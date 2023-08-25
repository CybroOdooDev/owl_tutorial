{
    'name': "Odoo App",
    'version': '16.0.1.0.0',
    'summary': 'Odoo App',
    'depends': [
        'base'
    ],
    'author': "Cybrosys",
    'category': 'Sales',
    'data': [
        'views/odoo_app_actions.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_app/static/src/js/*.*',
            'odoo_app/static/src/xml/*.*',
            'odoo_app/static/src/scss/app.scss',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}