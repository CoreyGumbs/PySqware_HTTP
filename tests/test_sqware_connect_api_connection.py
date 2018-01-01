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

#Test of Sq_Connect Module
class Test_Sq_Connect_Api_Connection(object):
	'''
	Testing of the Sq_connect module. Currently uses the square sandbox application ID and Access Token.

	'''
	@classmethod
	def setup_class(cls):
		#create class instance of Sq_Connect
		cls.sq_connect = Sq_Connect()

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

	# def test_api_connection_error_exceptions(self):
	# 	'''
	# 	Test the error exceptions of sq_connect().
	# 	'''
	# 	#returns string of HTTPError()
	# 	error_response_404 = self.sq_connect.get('/v2/locations/')
	# 	error_response_500 = self.sq_connect.get('/v5/locations')

	# 	#checks for common http errors.
	# 	assert error_response_404 == '404 Client Error: Not Found for url: https://connect.squareup.com/v2/locations/'
	# 	assert error_response_500 == '500 Server Error: Internal Server Error for url: https://connect.squareup.com/v5/locations'

	def test_api_post(self):
		'''
		Test Sq_Connect.post using get_categories method

		'''
		#gets categories for individual store location.
		query_item = get_categories(self.sq_connect.location_id)
		
		posted = self.sq_connect.post('/v2/catalog/search', {'id':query_item[0]['id']})
		
		assert query_item[0]['name'] == 'Smoothies'
		assert posted.status_code == requests.codes.ok





	


	


 