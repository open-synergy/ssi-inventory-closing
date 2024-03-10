# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models, api
from odoo.exceptions import ValidationError


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
        string="Queue Job",
        copy=False,
    )
    job_state = fields.Selection(
        string="Queue Job Status",
        related="job_id.state",
        store=True
    )
    job_result = fields.Text(
        string="Queue Job Result",
        compute="_get_job_result",
        store=False
    )

    def action_queue_job(self):
        print('\n action_queue_job')
        self.ensure_one()
        self.write(self._prepare_done_data())
        self._run_post_done_check()
        self._run_post_done_action()

    def action_done(self):
        for record in self.sudo():
            record._run_pre_done_check()
            record._run_pre_done_action()
            record.with_delay().action_queue_job()
