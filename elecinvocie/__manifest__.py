{
    'name': 'elecinvocie',
    'description': 'elecinvocie',
    'author': '',
    'depends': ['base','account','account_accountant','l10n_sa'],
    'application': True,
    'data': [

    #'security/elecinvocie_access.xml',
    'security/ir.model.access.csv',
    'views/ir_ui_view.xml',
    #'views/ir_actions_act_window.xml',
    
    
    #'views/ir_ui_menu.xml',
     'views/reports/invoice.xml',
     'views/reports/sampleinvocie.xml',
     #'views/reports/sampleinvociepos.xml',
     'data/data.xml',
    
        ],
    'installable':True
}
