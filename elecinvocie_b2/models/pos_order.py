# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string
import requests
import qrcode
import base64
from io import BytesIO
import hashlib

import logging
_logger = logging.getLogger(__name__)


class pos_order (models.Model):
    _inherit = 'pos.order'
    qr_unique_code = fields.Char(string='Code',index=True)

    



    #@api.onchange('qr_unique_code')
    # def generate_qr_code(self):
    #     qr = qrcode.QRCode(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_L,
    #         box_size=10,
    #         border=4,
    #     )

    #     qr_sample = qrcode.QRCode(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_L,
    #         box_size=10,
    #         border=4,
    #     )
    #     base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
    #     self.qr_link = base_url+"/invoicetax?invociekey=" +str(self.qr_unique_code ) #str(self.id).replace("NewId_","")
    #     self.qr_link_sample = base_url+"/sampleinvoicetax?invociekey=" +str(self.qr_unique_code )#+str(self.id).replace("NewId_","")
        
    #     qr.add_data(self.qr_link)
    #     qr.make(fit=True)
    #     img = qr.make_image()
    #     temp = BytesIO()
    #     img.save(temp, format="PNG")
    #     qr_image = base64.b64encode(temp.getvalue())
        
    #     qr_sample.add_data(self.qr_link_sample)
    #     qr_sample.make(fit=True)
    #     img_sample = qr_sample.make_image()
    #     temp_sample = BytesIO()
    #     img_sample.save(temp_sample, format="PNG")
    #     qr_image_sample = base64.b64encode(temp_sample.getvalue())
        
        
        
    #     self.qr_code = qr_image
    #     self.qr_code_sample = qr_image_sample
    #     self.isqrgenreated = True



    # def write(self, vals):
    #     # if not self.isqrgenreated:
    #     #     self.generate_qr_code()
        
    #     return super().write(vals)
  

    # @api.onchange('name')
    def generate_qr_unique_code(self):
        try:
            for rec in self :
                #cust_id=self.env['ir.config_parameter'].sudo().get_param('CUSTOMER_INV_ID')
                rec.qr_unique_code = hashlib.md5((rec.name.replace("/","_") +cust_id).encode()).hexdigest()
                
                #rec.generate_qr_code()
        except:
            pass
    

    def write(self, vals):
        #vals["qr_unique_code"] =hashlib.md5(vals["pos_reference"].encode()).hexdigest()
        rec= super().write(vals)
        try:
            if self.pos_reference and not self.qr_unique_code:
                self.qr_unique_code = hashlib.md5(self.pos_reference.encode()).hexdigest()
        except:
            pass

        return rec
    # def action_post(self):
    #     for rec in self :
    #         res = super(elecinvocie,rec).action_post()
    #         rec.generate_qr_unique_code()
    #         return res
    

    # def _post(self,soft=True):
    #     for rec in self :
    #         res = super(elecinvocie,rec)._post()
    #         rec.generate_qr_unique_code()
    #         return res
  
  
