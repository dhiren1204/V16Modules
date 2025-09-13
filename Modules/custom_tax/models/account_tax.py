from odoo import api, fields, models


class AccountTax(models.Model):
    _inherit = 'account.tax'

    @api.model
    def _prepare_base_line_for_taxes_computation(self, record, **kwargs):
        res = super()._prepare_base_line_for_taxes_computation(record, **kwargs)
        if record and record._name in ['account.move.line']:
            if record.custom_tax_percentage:
                custom_tax_amount = record.custom_tax_percentage
                custom_tax_amount = {str(record.company_id.custom_tax_id.id):{'tax_amount_currency':custom_tax_amount}}
                res.update({'manual_tax_amounts':custom_tax_amount})
        return res

    @api.model
    def _prepare_tax_line_for_taxes_computation(self, record, **kwargs):
        res = super()._prepare_tax_line_for_taxes_computation(record, **kwargs)
        if record and record._name in ['account.move.line']:
            tax_id = record.tax_repartition_line_id.tax_id
            if tax_id == record.company_id.custom_tax_id:
                aml_custom_percentage = record.move_id.invoice_line_ids.filtered(lambda x:x.custom_tax_percentage > 0.0)
                total_amount_currency = 0.0
                for aml in aml_custom_percentage:
                    result = self._prepare_base_line_for_taxes_computation(aml)
                    if result.get('manual_tax_amounts', {}).keys():
                        total_amount_currency += result['manual_tax_amounts'][str(tax_id.id)]['tax_amount_currency']
                sign = kwargs.get('sign', 1)
                res['amount_currency'] = total_amount_currency * sign
                res['balance'] = total_amount_currency * sign
        return res