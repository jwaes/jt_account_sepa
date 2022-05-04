from odoo import api, models, fields, _

class AccountBatchPayment(models.Model):
    _inherit = 'account.batch.payment'

    # Override the default to false ... 
    sct_batch_booking = fields.Boolean(default=False)