{
    'name': 'elecinvocie_b2',
    'description': 'elecinvocie_b2',
    'author': '',
    'depends': ['elecinvocie', 'point_of_sale'],
    'application': True,
    'data': [

        # 'security/elecinvocie_access.xml',
        # 'security/ir.model.access.csv',
        'views/ir_ui_view.xml',
        # 'views/ir_actions_act_window.xml',


        # 'views/ir_ui_menu.xml',

        'views/reports/sampleinvociepos.xml',
        'views/pos_assets.xml',


    ],
    'qweb': [
        'static/src/xml/pos_demo.xml',
        #'static/src/xml/pos.xml',
    ],
    'installable': True
}
