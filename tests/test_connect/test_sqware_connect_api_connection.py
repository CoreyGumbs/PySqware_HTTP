	#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the SqWare package Sq_Connect Class.
'''

import pytest
import requests 
import json
from sqware.connect import Sq_Connect
from sqware.catalog import get_categories
from sqware.customer import Sq_Customer

#Test of Sq_Connect Module
class Test_Sq_Connect_Api_Connection(object):
	'''
	Testing of the Sq_connect module. Currently uses the square sandbox application ID and Access Token.

	'''

	@classmethod
	def setup_class(cls):
		#create class instance of Sq_Connect
		cls.sq_connect = Sq_Connect()
		#customer instance
		cls.customer = Sq_Customer(
			first_name = "John",
			last_name = "Times",
			email = "tim@testing.com",
			phone = "1-123-345-1234"
			)

	def test_api_connection(self):
		'''
		Test the connection to square api for user account.
		Remember to change  ACCESS_TOKEN in secrets file to either sandbox or production api access token provided via square.

		'''
		#Establish connection to square api
		#returns response object that uses Requests module api
		locations = self.sq_connect.get('/v2/locations')
	
		#checks for https connection to square api
		assert locations.status_code == requests.codes.ok

		#checks for correct url path
		assert locations.url == 'https://connect.squareup.com/v2/locations'

	def test_api_post(self):
		'''
		Test Sq_Connect.post using get_categories method

		'''
		#gets categories for individual store location.
		query_item = get_categories()
		
		posted = self.sq_connect.post('/v2/catalog/search', {'id':query_item[0]['id']})
		
		assert query_item[0]['name'] == 'Smoothies'
		assert posted.status_code == requests.codes.ok

	def test_api_connection_error_exceptions(self):
		'''
		Test the error exceptions of sq_connect().
		'''
		#returns string of HTTPError()
		error_response_404 = self.sq_connect.get('/v2/locations/')
		error_response_500 = self.sq_connect.get('/v5/locations')
		error_response_post = self.sq_connect.post('/v2/catalog/search/theonering', {'id': '13ascvei'})

		#checks for common http errors.
		assert error_response_404 == '404 Client Error: Not Found for url: https://connect.squareup.com/v2/locations/'
		assert error_response_500 == '500 Server Error: Internal Server Error for url: https://connect.squareup.com/v5/locations'
		assert error_response_post == '404 Client Error: Not Found for url: https://connect.squareup.com/v2/catalog/search/theonering'

	def test_api_put(self):
		'''
		Test Sq_Connect.put for updating account info.
		'''
		self.data = {
			'given_name': 'Charles',
			'email_address': self.customer.email,
			'address': {
				'address_line_1': '1234 New Street',
				'locality': 'Boston',
				'administrative_district_level_1': 'MA',
				'postal_code': '12345',
				'country': 'US'
			}
		}
		self.get_customer = self.customer.check_customer_email(self.customer.email)
		self.update = self.sq_connect.put('/v2/customers/' + self.get_customer['id'], self.data)

		assert self.get_customer['given_name'] == self.data['given_name']
		assert self.get_customer['address']['locality'] ==  self.data['address']['locality']

	def test_api_delete(self):
		'''
		Test Sq_Connect.delete for deleting account.
		'''
		self.dummy_customer = Sq_Customer(
			first_name = 'Delete',
			last_name = 'Dummy',
			email = 'test_data@testing.com',
			phone = '123-345-4566'
		)
		self.test_customer = self.dummy_customer.create_customer(self.dummy_customer.custmr_data)
		self.get_customer = self.dummy_customer.check_customer_email(self.dummy_customer.email)
		self.deleted = self.sq_connect.delete('/v2/customers/' + self.get_customer['id'])

		assert self.get_customer['given_name'] == self.dummy_customer.first_name
		'''
		The Square API returns a json response object of "{}" or an empty dict.
		This tests whether the response object converted into json returns and empty dict or not.
		Bool() will return false if dict empty.
		Uses the .json() of the requests library to render dict in json.
		'''
		assert bool(self.deleted.json()) ==  False