from odoo import api, fields, models
from odoo.api import readonly


class ResCompany(models.Model):
    _inherit = 'res.company'

    custom_tax_id = fields.Many2one('account.tax', 'Custom Tax', )


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    custom_tax_id = fields.Many2one('account.tax', 'Custom Tax', related='company_id.custom_tax_id',
                                    readonly=False)
