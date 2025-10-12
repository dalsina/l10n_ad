from odoo import Command, _, models
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('ad')
    def _get_ad_template_data(self):
        return {
            'name': _('Base'),
            'visible': False,
            'code_digits': '8',
            'property_account_receivable_id': 'l10n_ad.account_common_430',
            'property_account_payable_id': 'account_common_400',
            'downpayment_account_id': 'account_common_485',
        }

    @template('ad', 'res.company')
    def _get_ad_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.ad',
                'bank_account_code_prefix': '572',
                'cash_account_code_prefix': '570',
                'transfer_account_code_prefix': '555',
                'account_default_pos_receivable_account_id': 'l10n_ad.account_common_430',
                'income_currency_exchange_account_id': 'account_common_768',
                'expense_currency_exchange_account_id': 'account_common_668',
                'account_journal_suspense_account_id': 'account_common_5729',
                'account_journal_early_pay_discount_loss_account_id': 'account_common_706',
                'account_journal_early_pay_discount_gain_account_id': 'account_common_606',
                'account_sale_tax_id': 'account_tax_template_s_igi45',
                'account_purchase_tax_id': 'account_tax_template_p_igi45',
                'account_purchase_receipt_fiscal_position_id': 'fp_general',
                'default_cash_difference_income_account_id': 'account_common_768',
                'default_cash_difference_expense_account_id': 'account_common_668',
                'transfer_account_id': 'account_common_555',
                'expense_account_id': 'account_common_600',
                'income_account_id': 'account_common_700',
            },
        }
