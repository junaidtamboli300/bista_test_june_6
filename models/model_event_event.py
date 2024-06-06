from odoo import api,fields,models,_

class Event_event(models.Model):
    _name = "event.events"
    _description = "These are the event.event"
    
    name = fields.Char(string="Name")
    description = fields.Text(string = "Description")
    start_date = fields.Datetime(string = "start date")
    end_date = fields.Datetime(string = "End date")
    organizer_id = fields.Many2one('event.oraginer',string = "Organizer ID")
    attendee_ids = fields.Many2many('event.attendee',string = "Attendee IDS")
    duration = fields.Float(string='Duration (Days)', compute='_compute_duration')
    
    @api.depends('start_date', 'end_date')
    def _compute_duration_days(self):
        for event in self:
            if event.start_date and event.end_date:
                start_datetime = fields.Datetime.from_string(event.start_date)
                end_datetime = fields.Datetime.from_string(event.end_date)
                duration_days = (end_datetime - start_datetime).days + 1  # Add 1 to include both start and end days
                event.duration_days = duration_days
            else:
                event.duration_days = 0.0
                
    def _compute_attendee_count(self):
        for event in self:
            event.attendee_count = len(event.attendee_ids)
            
    def action_view_attendees(self):
        action = self.env.ref('event.action_event_attendees').read()[0]
        action['domain'] = [('id', 'in', self.attendee_ids.ids)]
        return action
    
    













    
    