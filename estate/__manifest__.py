{
    'version': '1.0',
    'name': 'Estate',
    'depends': ['base'],
    'author': 'Your Name',
    'category': 'Real Estate',
    'description': "Manage properties for sale or rent",
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',  # must come after estate_property_views.xml
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
