{
    'name': "RFQ Comparison Report",
    'summary': "RFQ Comparison Report",
    'description': """
        RFQ Comparison report showing product wise comparison against each vendor 
    """,
    "license": "LGPL-3",
    'author': "Sybaz",
    'website': "https://sybaz.com/",
    'category': 'Purchase/Purchase',
    'version': '17.0.1.0.1',
    'depends': ['purchase'],

    'data': [
        'views/purchase_order_views.xml',
        'views/purchase_comparison_templates.xml',
        'views/purchase_comparison_templates_pdf.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    'application': False,
    'installable': True,
    'auto_install': False,
    'price': 20,
    'currency': 'USD',
}
