{
    'name': 'elecinvocie',
    'description': 'elecinvocie',
    'author': '',
    'depends': ['base','account','sale_management','l10n_generic_coa'],
    'application': True,
    'data': [

    #'security/elecinvocie_access.xml',
    #'security/ir.model.access.csv',
    #'views/ir_ui_view.xml',
    #'views/ir_actions_act_window.xml',
    
    
    #'views/ir_ui_menu.xml',
     'views/reports/invoice.xml',
     'views/reports/sampleinvocie.xml',
    
        ],
    'installable':True
}
