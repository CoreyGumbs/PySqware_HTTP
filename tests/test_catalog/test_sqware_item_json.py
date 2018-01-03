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
from sqware.catalog import get_categories, Sq_Products, ItmJson

class Test_Catalog_ItmJson(object):
	'''
	'''
	@classmethod
	def setup_class(cls):
		cls.connect = Sq_Connect()
		cls.products = Sq_Products()
		cls.directory_path = '/Users/cgumbs/Devs/projects/pysqware_http/PySqware/sqware/catalog/json'
		cls.items = ItmJson(
			directory_path=cls.directory_path
			)

	def test_get_data(self):
		'''
		Test of json data from square items api.
		'''
		self.json_items = self.items.get_data()

		#test string in json data
		#assert 'objects' in self.json_items
		self.json_items

	def test_write_json_data(self):
		'''
		Test json data written to file
		'''
		pass