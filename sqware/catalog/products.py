#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Retrieve items associated with a particular category ID.

'''
import json
from sqware.catalog import ItmJson

class Sq_Products(object):
	'''
	Products class.
	'''
	def __init__(self):
		self.item_json = ItmJson()
		self.file_name = self.item_json.dir_path + 'json/items.json'

	def __str__(self):
		return '{}'.format('Sq_Products Module')

	def get_category_items(self, category_id):
		'''
		Retrieves items associated with selected category_id
		'''
		#retrieve all items from json file.
		# self.json_data = self.item_json.retrieve_json()
		
		try:
			#products results container 
			self.category_items = []

			with open(self.file_name, 'r') as file_data:		
				#loops through json data and returns associated items.
				data = json.loads(file_data.read())
				for products in data['objects']:
					for key, value in products['item_data'].items():
						if category_id == value:
							self.category_items.append(products)

			#if products are placed in list, returns list
			if self.category_items:
				return self.category_items

		except IOError as e:
			return str(e)



	


		