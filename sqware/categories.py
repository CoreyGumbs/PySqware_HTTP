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
		self.location = self.connection.location_id

	def connect_catalog(self, request_path):
		#establish connection to catalog endpoints
		catalog_endpoint = self.connection.get(request_path)
		return catalog_endpoint

	def retrieve_catalog_categories(self, location_id):
		'''
		Retrieves categories from json data and returns them in a simple dictionary.
		'''
		#catalog list endpoint
		category_endpoint = self.connection.get('/v1/' + location_id + '/categories')

		#retrieves and decodes returned json data
		category_data = category_endpoint.json()
		
		# return category_data
		return category_data

	def retrieve_category_items(self, cat_id, cat_name=None):
		'''
		Filters items from JSON data associated with requested catalog id.
		Will return None if wrong ID or no items associated with ID are returned.
		'''	
		try:
			#connects to square api
			print(cat_name)
			category_item_endpoint =  self.connection.get('/v2/catalog/list?types=item')
			
			#decode JSON data
			category_item_json = category_item_endpoint.json()

			#products results list 
			category_items = []
			#loops through json data and returns associated items.
			for products in category_item_json['objects']:
				for key, value in products['item_data'].items():
					if cat_id == value:
							category_items.append(products)

			#if products are placed in list, returns list
			if category_items:
				return category_items
		except:
			#returns None if there are no products associated with cat_id
			return None



				
	
	

	 




