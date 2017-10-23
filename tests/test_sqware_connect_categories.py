#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the SqWare package Sq_Connect Class.
'''

import pytest
import requests 
import json
from sqware.categories import Sq_Catalog

#Test of Sq_Connect Catagories Functionality
class Test_Sq_Connect_Catalog(object):
	'''
	Testing of the Sq_connect catagories functionality. Currently uses the square sandbox application ID and Access Token.

	'''
	@classmethod
	def setup_class(cls):
		#create class instance of Sq_Categories
		cls.sq_category = Sq_Catalog()

	def test_catalog_api_connection(self):
		'''
		Test for the categories list endpoint and connection.
		'''
		catalog = self.sq_category.retrieve_catalog_categories('/v2/catalog/list')
	
		assert catalog.status_code == requests.codes.ok
		assert catalog.url == 'https://connect.squareup.com/v2/catalog/list'

	def test_catalog_category_retrieval(self):
		catalog = self.sq_category.retrieve_catalog_categories('/v2/catalog/list')

		assert catalog == {'objects': [{'catalog_v1_ids': [{'catalog_v1_id': 'cd346e2f-352c-48d6-b19b-1dc26ef1fa5c', 'location_id': '1R6PMMJ61ZW...63700dc60822a7b3b7543f0bb5a/original.png', 'label_color': '0b8000', ...}, 'present_at_all_locations': True, ...}, ...]}


