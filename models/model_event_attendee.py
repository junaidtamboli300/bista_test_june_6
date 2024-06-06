from odoo import api,fields,models,_

class Event_attendee(models.Model):
    _name = "event.attendee"
    _description = "These are the event.attendee"
    
    name = fields.Char(string="Name")
    email = fields.Char(string = "Email")
    phone = fields.Char(string = "Phone")
    user_id = fields.Many2one(string  = "User id" ,readonly = "True")
    event_ids = fields.Many2many('event.events')
    
       