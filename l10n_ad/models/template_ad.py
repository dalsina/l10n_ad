from odoo import models
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('ad')
    def _get_ad_template_data(self):
        raise Exception("¡La función se ejecuta 1!")
        return {
            'property_account_receivable_id': 'l10n_ad.account_common_430',
            'property_account_payable_id': 'l10n_ad.account_common_400',
            'currency_id': 'base.EUR',
            'country_id': 'base.ad',
            'code_digits': '8',
        }

    @template('ad', 'res.company')
    def _get_ad_res_company_data(self):
        raise Exception("¡La función se ejecuta! 2")
        return {
            self.env.company.id: {
                'account_sale_tax_id': 'l10n_ad.account_tax_template_s_igi45',
                'account_purchase_tax_id': 'l10n_ad.account_tax_template_p_igi45',
                'bank_account_code_prefix': '572',
                'cash_account_code_prefix': '570',
                'transfer_account_code_prefix': '57299',
                'account_fiscal_country_id': 'base.ad',
            }
        }
