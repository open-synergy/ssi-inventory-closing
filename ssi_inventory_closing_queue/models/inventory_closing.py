# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class InventoryClosing(models.Model):
    _inherit = "inventory_closing"

    job_id = fields.Many2one(
        comodel_name="queue.job",
        string="Queue Job",
        required=False,
    )
