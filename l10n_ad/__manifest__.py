{
    "name": "Andorra - Comptabilitat",
    "author": "Tècniques d'Avantguarda (TdA)",
    "website": 'https://repo.tda.ad/odoo/l10n-andorra',
    "category": "Localization/Account Charts",
    "version": "19.0.1.0.0",
    "depends": [
        "account",
        "base_vat",
        "base_iban",
        # "l10n_ad_defaults",
    ],
    "data": [
        "data/account_chart_template.xml",
        'data/account.account-full.csv',
        'data/account.account-common.csv',
        "data/fiscal_positions-ad.xml",
        "data/account_tax_group-ad.xml",
        "data/account_tax-ad.xml",
    ],
    'installable': True,
    'images': [
        'images/config_chart_l10n_es.png',
        'images/l10n_es_chart.png'
    ],
}
