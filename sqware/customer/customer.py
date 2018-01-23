#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from types import *
from sqware.connect import Sq_Connect


class Sq_Customer(object):
	'''
	Square Customer Class
	'''
	def __init__(self, first_name, last_name, email, phone):
		'''x
		'''
		self.connect =  Sq_Connect()
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone = phone
		self.custmr_data = {
			'given_name' : self.first_name,
			'family_name': self.last_name,
			'email_address': self.email,
			'phone_number': self.phone
			
		}


	def __repr__(self):
		return '{}{}{}'.format('Customer: ', self.first_name, self.last_name)

	def __str__(self):
		return '{}{}{}'.format('Customer: ', self.first_name, self.last_name)

	def __sqware_json_decoder(self, response_obj):
		'''
		Creates useable json data from square json response object.
		'''
		if isinstance(response_obj, str):
			return '{}'.format('Customer not found. Please try again.')
		else:
			self.retrieved_data = response_obj.json()
			self.json_data = json.dumps(self.retrieved_data, sort_keys=False, indent=4)
			self.customer_json = json.loads(self.json_data)
			return self.customer_json

	def __get_customer_json(self):
		'''
		Retrieves JSON response object from square api. 
		'''
		#gets data from square catalog endpoint
		self.get_data = self.connect.get('/v2/customers')
		#returns decoded json data
		return self.__sqware_json_decoder(self.get_data)

	def check_customer(self, user_email):
		'''
		Checks if customer already exists in square.
		'''
		self.customer_email =  self.__get_customer_json()
		
		for items in self.customer_email['customers']:
			if user_email in items.get('email_address'):
				return items
		return False

	def get_customer(self, user_id):
		'''
		Retrieves customer data from square api.
		'''
		self.get_data = self.connect.get('/v2/customers/' + user_id)
		return self.__sqware_json_decoder(self.get_data)

	def create_customer(self, data):
		'''
		Creates customer
		'''
		if not self.check_customer(data['email_address']):
			self.create_customer = self.connect.post('/v2/customers', data)
			return self.check_customer(data['email_address'])
		else:
			return self.check_customer(data['email_address'])
			




	
	
		





		
			
			


