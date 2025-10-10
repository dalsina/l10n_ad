{
    'name': "Exportar Llibre IGI",
    'summary': "Amb aquest mòdul podem exportar a Excel els llibres d'IGI corresponents.",
    'author': "Tècniques d'Avantguarda (TdA)",
    "website": 'https://repo.tda.ad/odoo/l10n-andorra',
    "category": "Localization/Account Charts",
    'version': '19.0.1.0.0',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/l10n_ad_vat_book.xml',
    ],
    'external_dependencies': {
        'python': ['openpyxl']
    },
    'installable': True,
}
