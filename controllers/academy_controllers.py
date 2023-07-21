from odoo import http
class Academy(http.Controller):
    @http.route('/academy/')
    def index(self, **kw):
        return 'Hello World'