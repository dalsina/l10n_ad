from odoo import _, models
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('ad_comp')
    def _get_ad_comp_template_data(self):
        return {
            'name': _('Empreses'),
            'parent': 'ad',
            'code_digits': '8',
            'sequence': 0,
        }

    @template('ad_comp', 'res.company')
    def _get_ad_comp_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.ad',
                'bank_account_code_prefix': '572',
                'cash_account_code_prefix': '570',
                'transfer_account_code_prefix': '555',
            },
        }