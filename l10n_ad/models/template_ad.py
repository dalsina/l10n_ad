from odoo import models
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('ad')
    def _get_ad_template_data(self):
        return {
            'template_data': {
                'property_account_receivable_id': 'l10n_ad.account_common_430',
                'property_account_payable_id': 'l10n_ad.account_common_400',
                'code_digits': '8',
                'currency_id': 'base.EUR',
                'country_id': 'base.ad',
            }
        }