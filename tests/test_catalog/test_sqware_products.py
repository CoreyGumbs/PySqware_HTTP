	#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the Sqware package Sq_Products Class.
'''
import os
import pytest
import requests 
import json
from sqware.connect import Sq_Connect
from sqware.catalog import get_categories, Sq_Products

class Test_Catalog_Products(object):
	'''
	'''
	@classmethod
	def setup_class(cls):
		cls.connect = Sq_Connect()
		cls.products =  Sq_Products()

	def test_get_products_json_data(self):
		'''
		Test that json data is retrieved and saved to a dir/file.
		'''
		json_items = self.products.get_json_data()

		assert 'objects' in json_items


		

