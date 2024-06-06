{
    'name' : 'event management system',
    'author':'junaid',
    'website' : 'odoomates.com',
    'summary' : 'odoo16',
    'depends' : ['base'],
    
    'data':[
        'security/ir.model.access.csv',
        'views/event_registration.xml',
        'views/event_event.xml',
        'views/event_attendee.xml',
        'views/event_organizer.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    
}