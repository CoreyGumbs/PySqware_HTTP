#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the SqWare package Sq_Connect Class.
'''

import pytest
import requests 
import json
from sqware.connection import Sq_Connect

#Test of Sq_Connect Catagories Functionality
class Test_Sq_Connect_Catalog(object):
	'''
	Testing of the Sq_connect catagories functionality. Currently uses the square sandbox application ID and Access Token.

	'''
	@classmethod
	def setup_class(cls):
		#create class instance of Sq_Connect
		cls.sq_connect = Sq_Connect()

	def test_api_connection(self):
		'''
		Test for the categories endpoint and connection.
		'''
		catalog = self.sq_connect.connect_api('/v2/catalog/list')
		assert catalog.status_code == requests.codes.ok

	def test_catalog_list_retriveal(self):
		'''
		'''
		pass
