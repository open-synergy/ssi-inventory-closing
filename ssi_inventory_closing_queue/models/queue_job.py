# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models, api


class QueueJob(models.Model):
    _inherit = "queue.job"

    def write(self, vals):
        res = super(QueueJob, self).write(vals)
        for rec in self:
            if vals.get('state') in ['cancelled', 'failed'] and rec.model_name == 'inventory_closing':
                for closing_id in rec.records.filtered(lambda c: c.state == 'confirm'):
                    sorted_approval_ids = closing_id.approval_ids.sorted(key='date', reverse=True)
                    last_approval_id = sorted_approval_ids[:1]
                    last_approval_id.write({
                        'status': 'pending',
                        'user_id': False,
                        'date': False,
                    })
        return res
