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
		catalog_endpoint = self.connect_catalog(request_path)
		#retrieves and decodes returned json data
		catalog_data = catalog_endpoint.json()
		#looks for catalog items with 'catalog_data' key and creates a list of json objects
		data = [category for category in catalog_data['objects'] if 'category_data' in category]

		#empty dictionary for category name, id, and updated key/value pairs
		category_data = {}

		#Extracts catalog information from json object and creates key/value pairs
		for item in range(len(data)):
			category_data[item] = { 'name': data[item]['category_data']['name'], 'id': data[item]['id'], 'updated': data[item]['updated_at']}

		return category_data