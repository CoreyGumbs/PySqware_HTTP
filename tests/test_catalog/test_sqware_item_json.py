	#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the Sqware package Sq_Products Class.
'''
import pytest
import requests 
import json
from sqware.connect import Sq_Connect
from sqware.catalog import get_categories, Sq_Products, ItmJson

class Test_Catalog_ItmJson(object):
	'''
	'''
	@classmethod
	def setup_class(cls):
		cls.connect = Sq_Connect()
		cls.products = Sq_Products()
		cls.items = ItmJson()

	def test_get_item_json(self):
		'''
		Test of json data from square items api.
		'''
		self.json_items = self.items.get_item_json()

		#test string in json data
		assert 'objects' in self.json_items

	def test_write_json_data(self):
		'''
		Test json data written to file
		'''
		pass