from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    custom_tax_percentage = fields.Float('Custom Tax Percentage', )

    @api.onchange('custom_tax_percentage')
    def _onchange_custom_tax_percentage(self):
        custom_tax_id =self.company_id.custom_tax_id.id
        if not custom_tax_id:
            self.message_post(body=f'Please configure custom tax to apply custom tax amount')
        else:
            existing_taxes = self.tax_ids.ids
            if self.custom_tax_percentage:
                if not custom_tax_id in existing_taxes:
                    existing_taxes.append(custom_tax_id)
            else:
                if custom_tax_id in existing_taxes:
                    existing_taxes.remove(custom_tax_id)
            self.tax_ids = existing_taxes
