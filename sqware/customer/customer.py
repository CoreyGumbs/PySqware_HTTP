#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from types import *
from sqware.connect import Sq_Connect


class Sq_Customer(object):
	'''
	'''
	def __init__(self, first_name, last_name, email, phone):
		'''x
		'''
		self.connect =  Sq_Connect()
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone = phone

	def __str__(self):
		pass

	def __get_item_json(self):
		'''
		Retrieves JSON data for all customers. 
		'''
		#gets data from square catalog endpoint
		self.get_data = self.connect.get('/v2/customers')
		#decodes json data
		self.retrieved_data = self.get_data.json()
		#prettifies json data
		self.json_data = json.dumps(self.retrieved_data, sort_keys=False, indent=4)
		return self.json_data


	def check_customer(self, user_email):
		'''
		Checks if customer already exists in square.
		'''
		self.get_json =  self.__get_item_json()
		self.customer_email = json.loads(self.get_json)
		
		for items in self.customer_email['customers']:
			if user_email in items.get('email_address'):
				return True
		return False
		

		





		
			
			


