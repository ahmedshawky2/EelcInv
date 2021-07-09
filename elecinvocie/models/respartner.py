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


class rescompany (models.Model):
    _inherit = 'res.partner'

    building_number = fields.Char(string='Building Number')
    postal_code = fields.Char(string='Postal Code')
    additional_no = fields.Char(string='Additional No.')
    other_seller_id = fields.Char(string='Other Seller ID')
