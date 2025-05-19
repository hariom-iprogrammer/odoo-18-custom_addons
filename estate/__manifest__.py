{
    'version': '1.0',
    'name': 'Estate',
    'depends': ['base'],
    'author': 'Your Name',
    'category': 'Real Estate',
    'description': "Manage properties for sale or rent",
    'data': [
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
