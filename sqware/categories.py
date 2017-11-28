#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Retrieve Categories, search for items in category, and returns items.

'''

import json
import requests
from collections import OrderedDict
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
		catalog_endpoint = self.connection.get('/v1/' + location_id + '/categories')
		
		#retrieves and decodes returned json data
		catalog_data = catalog_endpoint.json()
		
		# return category_data
		return catalog_data

	def retrieve_category_items(self, category_id_num):
		'''
		'''
		# data = {
		# 	"object_types": [
		# 		"ITEM"
		# 	]
		# }
		data = {
			"object_ids": [category_id_num],
			"include_related_objects": True
		}

		post_data = self.connection.post('/v2/catalog/batch-retrieve', data)

		items_data = post_data.json()
		items = json.dumps(items_data, sort_keys=True, indent=4)
		#test_run = json.loads(items_data, object_pairs_hook=OrderedDict)
		#new_data = [x for x in items_data['objects']]
		
		category_item = {}
		# for item in new_data:
		# 	if item['id'] == category_id_num:
		# 		print(item['id'], str("'"+category_id_num+"'"))
		# 	else:
		# 		 print(('there is no category with the id: {}').format({category_id_num}))
		# 
		print(items)

	 




