# -*- coding: utf-8 -*-
# from odoo import models, fields, api
# from odoo import exceptions
# from odoo.exceptions import ValidationError
# import json
# import datetime
# import string
# import requests

from typing import ValuesView
from odoo import http
from odoo.http import request


import logging
_logger = logging.getLogger(__name__)


class elecinvocie (http.Controller):
    @http.route('/invoice',website=True,auth='none')
    def invoice(self):
        return "1"

    
    


    @http.route('/sampleinvoicepoc', methods=['POST', 'GET'], csrf=False, type='http', auth="none", website=True)
    def sampleinvoicetax(self, **kw):
        invociekeycode = kw['invociekey']
        
        #return base_url
        #return invociekeycode
        recs = request.env['pos.order'].sudo().search([('qr_unique_code','=',invociekeycode)],limit=1)
        #invociekey = recs.id
        #return invociekey
        #recs = request.env['account.move'].sudo().search([('qr_unique_code','=',invociekeycode)],limit=1)
        
        invociekey = recs.account_move
        #return str(invociekey)
        invociekey = int(invociekey)
        #invociekey = int(invociekeycode)
        if invociekey:
            # pdf = request.env['report'].sudo().get_pdf([invociekey], 'elecinvocie.am_r_report_1', data=None)
            # pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
            # return request.make_response(pdf, headers=pdfhttpheaders)

            pdf = request.env.ref('elecinvocie.am_r_reportsample_1').sudo()._render_qweb_html([invociekey])[0]
            pdfhttpheaders = [
                ('Content-Type', 'application/pdf'),
                ('Content-Length', len(pdf)),
            ]
            return request.make_response(pdf)
        else:
            return "Wrong URL"


        