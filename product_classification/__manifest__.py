# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "product_classification",
    'summary': """
        Product Classification""",
    'description': """
        Fields for the classification of the product.
    """,
    'author': "gflores",
    'website': "https://www.gruporequiez.com",
    'category': 'Inventory',
    'version': '0.0.1',
    'depends': ['product', 'stock'],
    'data': [
        # views
        'views/product_template_view.xml',
        'views/stock_move_line_view.xml',
        # reports
    ],
    'demo': [
    ],
    'application': True,
}
