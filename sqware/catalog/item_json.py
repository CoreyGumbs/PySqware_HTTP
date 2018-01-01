#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from sqware.connect import Sq_Connect
from sqware.catalog import get_categories


class ItmJson(object):
	'''
	Item json data
	'''
	def __init__(self, category_id=None, category_name=None):
		self.connect = Sq_Connect()
		self.categories = get_categories(self.connect.location_id)
		self.cat_id = category_id
		self.cat_name = category_name

	def __str__(self):
		return '{} : {}'.format(self.cat_name, self.cat_id)

	def get_item_json(self):
		'''
		Retrieves JSON data for all items/products in square catalog. 
		'''
		#gets data from square catalog endpoint
		self.get_data = self.connect.get('/v2/catalog/list?types=item')
		#decodes json data
		self.json_data = self.get_data.json()
		return self.json_data
	
