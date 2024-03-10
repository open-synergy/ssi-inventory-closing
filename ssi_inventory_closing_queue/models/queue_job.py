# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models, api


class QueueJob(models.Model):
    _inherit = "queue.job"

    @api.model
    def create(self, values):
        res = super(QueueJob, self).create(values)
        if res.model_name == 'inventory_closing':
            res.records.write({
                'job_id': res.id
            })
        return res
