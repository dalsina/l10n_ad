{
    "name": "Andorra - Comptabilitat",
    "author": "IPGrup x IdeAnd",
    "category": "Accounting/Localizations/Account Charts",
    "version": "19.0.1.0.0",
    'icon': '',
    'countries': ['ad'],
    'depends': [
        "account",
        "base_vat",
        "base_iban",
    ],
    "data": [
        'data/account_chart_template.xml',
        'data/account.account-full.csv',
        'data/account.account-common.csv',
        'data/fiscal_positions-ad.xml',
        'data/account_tax_group-ad.xml',
        'data/account_tax-ad.xml',
    ],
    'installable': True,
    'images': [
        'images/config_chart_l10n_es.png',
        'images/l10n_es_chart.png'
    ],
    'l10n': True,
    'license': 'LGPL-3',
}
