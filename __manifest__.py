{
    'name': 'Odoo Academy',
    'summary' : 'Module to handel Course and Sessions',
    'description' : """Module to handle:
    - Courses
    - Sessions
    - Attendees
    """,
    'license' : 'OPL-1',
    'author' : 'Mauricio Rubio',
    'website' : 'www.odoo.com',
    'category' : 'Custom Modules / Technical Training',
    'depends' : ['base'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'data/session_data.xml',
        'views/academy_menu_items.xml',
        'views/course_views.xml',
        'views/sessions_views.xml'
    ],
    'demo': [
        'demo/course_demo.xml'
    ],
    'application' : True,

}   