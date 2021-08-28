# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string
import requests

import logging
_logger = logging.getLogger(__name__)


class elecinvociesetting (models.Model):
    _name = 'elecinvociesetting'
  
    
    name = fields.Char(string='Customer Name')
    bundle = fields.Char(string='Bundle Name')
    desc = fields.Text(string='Desc')


    

    
    





    
    



    
  
  
