	#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the Sqware package Sq_Products Class.
'''
import os
import pytest
import requests 
import json
from pathlib import Path
from sqware.connect import Sq_Connect
from sqware.catalog import get_categories, Sq_Products, ItmJson

class Test_Catalog_ItmJson(object):
	'''
	'''
	@classmethod
	def setup_class(cls):
		cls.connect = Sq_Connect()
		cls.products = Sq_Products()
		cls.directory_path = '/Users/cgumbs/Devs/projects/pysqware_http/PySqware/sqware/catalog/'
		cls.items = ItmJson(
			directory_path=cls.directory_path
			)

	def test_get_data(self):
		'''
		Test of creation of json directory and file(s).
		'''
		self.direct_path = Path(self.items.dir_path + 'json/')
		self.file_name = Path(self.items.dir_path + 'json/items.json')
		self.json_items = self.items.get_data()

		assert self.direct_path.exists() == True
		assert self.file_name.exists() == True

	def test_json_data_saved(self):
		'''
		Test Json data is saved.
		'''
		self.file_name = Path(self.items.dir_path + 'json/items.json')

		with open(self.file_name, 'r') as json_file:
			json_data = json.load(json_file)

		assert 'objects' in json_data
		assert 'category_id' in json_data['objects'][1]['item_data']




