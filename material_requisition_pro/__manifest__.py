{
    'name': 'Material Requisition Pro',
    'version': '18.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Material Requisition Management',
    'description': """
        Material Requisition Pro
        ========================
        This module provides material requisition functionality with proper field management.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'stock', 'product'],
    'data': [
        'data/sequence_data.xml',
        'security/ir.model.access.csv',
        'views/material_requisition_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}