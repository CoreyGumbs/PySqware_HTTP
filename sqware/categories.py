#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Retrieve Categories, search for items in category, and returns items.

'''

import json
import requests
from sqware.connection import Sq_Connect


class Sq_Catalog(object):
	def __init__(self):
		self.connection = Sq_Connect()

	def connect_catalog(self, request_path):
		#establish connection to catalog endpoints
		catalog_endpoint = self.connection.connect_api(request_path)
		return catalog_endpoint

	def retrieve_catalog_categories(self, request_path):
		#catalog list endpoint
		catalog_endpoint = self.connect_catalog(request_path +'?types=category')
		#retrieves and decodes returned json data
		catalog_data = catalog_endpoint.json()
		#looks for catalog items with 'catalog_data' key and creates a list of json objects
		data = [category for category in catalog_data['objects']]
		
		return data