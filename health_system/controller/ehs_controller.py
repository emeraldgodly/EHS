from odoo import http

class EhsRecords(http.Controller):
    @http.route('/ehs/login', methods=['POST'], auth='public', csrf=False)
    def login(self, **kwargs):
        print(kwargs)