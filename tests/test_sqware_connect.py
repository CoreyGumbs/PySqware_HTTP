	#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the SqWare package Sq_Connect Class.
'''

import pytest
import requests 
import json
from sqware.connection import Sq_Connect

#Test of Sq_Connect Module
class Test_Sq_Connect(object):
	'''
	Testing of the Sq_connect module. Currently uses the square sandbox application ID and Access Token.

	'''

	@classmethod
	def setup_class(cls):
		cls.sq_connect = Sq_Connect()

	def test_api_connection(self):
		'''
		Test the connection to square api for user account.
		Remember to change  ACCESS_TOKEN in secrets file to either sandbox or production api access token provided via square.

		'''
		#Establish connection to square api
		#returns response object that uses Requests module api
		locations = self.sq_connect.connect_api('/v2/locations')
		#checks for https connection to square api
		assert locations.status_code == 200

		#checks for correct url path
		assert locations.url == 'https://connect.squareup.com/v2/locations'



	


	


 