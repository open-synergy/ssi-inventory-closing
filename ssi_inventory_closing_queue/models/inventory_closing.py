# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

from odoo.addons.ssi_decorator import ssi_decorator


class InventoryClosing(models.Model):
    _inherit = "inventory_closing"

    @api.depends(
        "job_id.result",
        "job_id.exc_info",
    )
    def _get_job_result(self):
        for rec in self:
            rec.job_result = rec.job_id.result or rec.job_id.exc_info

    job_id = fields.Many2one(
        comodel_name="queue.job",
        string="Job",
        copy=False,
    )
    job_state = fields.Selection(
        string="Status",
        related="job_id.state",
        store=True
    )
    job_result = fields.Text(
        string="Result",
        compute="_get_job_result",
        store=False
    )

    @ssi_decorator.post_done_action()
    def _02_create_aml_from_svl(self):
        _super = super(InventoryClosing, self)
        if self.env.context.get('job_uuid'):
            _super._02_create_aml_from_svl()
            self.write({
                "state": "done",
            })
        else:
            update_vals = {
                "state": self._approval_state
            }
            if self.job_id:
                self.job_id.requeue()
            else:
                description = "Create job queue for %s" % self.name
                job = self.with_delay(description=_(description))._02_create_aml_from_svl()
                queue_job_obj = self.env["queue.job"]
                criteria = [("uuid", "=", job.uuid)]
                update_vals.update({
                    "job_id": queue_job_obj.search(criteria, limit=1, order="id desc").id,
                })
            self.write(update_vals)
