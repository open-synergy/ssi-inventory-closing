# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class InventoryClosing(models.Model):
    _inherit = "inventory_closing"

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

    def action_done(self):
        for record in self.sudo():
            record._run_pre_done_check()
            record._run_pre_done_action()
            # record.write(record._prepare_done_data())
            record.with_delay()._run_post_done_check()
            # record._run_post_done_action()
