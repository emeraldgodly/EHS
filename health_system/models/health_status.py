from odoo import models,fields,api
import datetime
from math import cos, asin, sqrt


class PatientRecords(models.Model):

    _name = 'incident.record'
    _rec_name = 'victim'

    # select = fields.Selection([('incident', 'Incident Observation'), ('injury', 'Human Injury')], string='Select', default='incident',
    #                           required=True)
    injury = fields.Boolean(string='injury')
    incident = fields.Boolean(string='incident')
    incident_type = fields.Many2one('res.partner',domain=[('victim','=','True')], string='Category')
    injury_intensity = fields.Selection([('0','Low'),('1','Normal'),('2','High'),('3','Very High'),('4','Severe'),('5','Death Stage')], string='Intensity', required=True)
    time = fields.Datetime(string='Incident Time')
    victim = fields.Many2one('res.partner',domain=[('victim_name','=','True')])
    location = fields.Selection([('internal','Internal'),('external','External')])
    step = fields.Text('First Step Done')

    describe = fields.Text('Describe the incident')
    company_id = fields.Many2one('res.company', string='Company')
    region = fields.Char('Region')
    city = fields.Char('City')
    street = fields.Char('Street')
    street_no = fields.Integer('Street No')
    locations = fields.Many2one('res.country',string='Location')
    latitude = fields.Float('latitude')
    longitude = fields.Float('Longitude')


    location_id = fields.Char('Company ID')
    country_emergency_no = fields.Char('Emergency Number')
    region_emergency_no = fields.Char('Region Emergency Number')


    image = fields.Binary('Add Image')
    image_1 = fields.Binary('Add Image')
    image_2 = fields.Binary('Add Image')
    image_3 = fields.Binary('Add Image')
    image_4 = fields.Binary('Add Image')
    image_5 = fields.Binary('Add Image')
    image_6 = fields.Binary('Add Image')
    image_7 = fields.Binary('Add Image')
    description1 = fields.Char('Describe')
    description2 = fields.Char('Describe')
    description3 = fields.Char('Describe')
    description4 = fields.Char('Describe')
    description5 = fields.Char('Describe')
    description6 = fields.Char('Describe')
    description7 = fields.Char('Describe')
    description8 = fields.Char('Describe')

    injury_damage = fields.Selection(
        [('0', 'Low'), ('1', 'Normal'), ('2', 'High'), ('3', 'Very High'), ('4', 'Severe'), ('5', 'Deathstage')],
        string='Intensity', required=True)
    injury_type = fields.Many2one('res.partner',domain=[('victim','=','True')], string='Category')
    times = fields.Datetime(string='Time')
    victim_name = fields.Many2one('incident.record', string='Name')
    place = fields.Selection([('internal', 'Internal'), ('external', 'External')])
    step1 = fields.Text('First Step Done')
    image1 = fields.Binary()
    image2 = fields.Binary()
    image3 = fields.Binary()
    image4 = fields.Binary()
    image5 = fields.Binary()
    image6 = fields.Binary()
    image7 = fields.Binary()
    image8 = fields.Binary()
    description9 = fields.Char()
    description10 = fields.Char()
    description11 = fields.Char()
    description12 = fields.Char()
    description13 = fields.Char()
    description14 = fields.Char()
    description15 = fields.Char()
    description16 = fields.Char()


    #
    # def distance(lat1, lon1, lat2, lon2):
    #     p = 0.017453292519943295
    #     a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    #     return 12742 * asin(sqrt(a))
    #
    # lat = 9.0516854
    # longi = 76.5360752
    #
    # base_cordinate = {'lat': lat, 'lon': longi}
    #
    # d = {8: [{'id': 8, 'latitude': '9.042418900000001', 'longitude': '76.5861815'}],
    #      9: [{'id': 9, 'latitude': '34.1047016', 'longitude': '-118.3338668'}],
    #      10: [{'id': 10, 'latitude': '8.5469144', 'longitude': '76.8792397'}]}
    #
    # def closest(data, v):
    #     return min(data, key=lambda p: distance(v['lat'], v['lon'], p['lat'], p['lon']))
    #
    # cord_list = []
    #
    # for k, v in d.items():
    #     new_lat = float(v[0]['latitude'])
    #     new_long = float(v[0]['longitude'])
    #
    #     cord_dict = {'lat': new_lat, 'lon': new_long}
    #     cord_list.append(cord_dict)
    #
    # closest_cordinate = closest(cord_list, base_cordinate)
    #
    # # To Get the id
    #
    # def fetch_id(base_dict, closest):
    #
    #     for key, val in d.items():
    #
    #         if float(val[0]['latitude']) == closest_cordinate['lat'] and float(val[0]['longitude']) == \
    #                 closest_cordinate['lon']:
    #             return val[0]['id']
    #
    # closest_cordinate['id'] = fetch_id(d, closest_cordinate)
    #
    # print(closest_cordinate)
    #







    # @api.onchange('victim')
    # def onchange_birthdate(self):
    #     if self.victim:
    #         self.country_emergency_no = self.victim.country_emergency_no
    #         self.region_emergency_no = self.victim.region_emergency_no
    #         self.location_id = self.victim.location_id
    #












class TestClass(models.Model):
    _inherit = 'res.partner'

    victim = fields.Boolean('Is Incident')
    victim_name = fields.Boolean('Is Victim')

    location_id = fields.Char('Company ID')
    country_emergency_no = fields.Char('Country Emergency Number')
    region_emergency_no = fields.Char('Region Emergency Number')




class TeamMembers(models.Model):

    _name = 'team_members.model'

    name = fields.Char('Name')




class ExternalLocation(models.Model):

    _name = 'external.location'

    location_id = fields.Char('Company ID')
    country_emergency_no = fields.Integer('Country Emergency Number')
    region_emergency_no = fields.Integer('Region Emergency Number')















