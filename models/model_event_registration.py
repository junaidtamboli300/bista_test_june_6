from odoo import api,fields,models,_

class Event_Registration(models.Model):
    _name = "event.registration"
    _description = "These are the event.registration"
     
    attendee_id = fields.Many2one('event.attendee',string = "attendee IDS")
    event_id = fields.Many2one('event.events',string = "Event IDS")
    registration_date = fields.Datetime(string = "Registration date")
     
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')],
        string="State", default='draft')

    def confirm_registration(self):
        self.write({'state': 'confirmed'})

    def cancel_registration(self):
        self.write({'state': 'cancelled'})
