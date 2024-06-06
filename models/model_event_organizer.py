from odoo import api,fields,models,_

class Event_organizer(models.Model):
    _name = "event.orgainzer"
    _description = "These are the event.organizer"
    
    name = fields.Char(string="Name")
    email = fields.Char(string = "Email")
    phone = fields.Char(string = "Phone")
    user_id = fields.Many2one('event.events',string = "User Ids" , readonly = True)
    event_ids = fields.One2many('event.events',string = "User Ids" , readonly = True)
    
    
    