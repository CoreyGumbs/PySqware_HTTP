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
from sqware.catalog import get_categories, ItmJson, CategoryJson 

class Test_Catalog_ItmJson(object):
	'''
	Test ItmJson Class
	'''
	@classmethod
	def setup_class(cls):
		cls.connect = Sq_Connect()
		#hard coded path of file
		cls.directory_path = '/Users/cgumbs/Devs/projects/pysqware_http/PySqware/sqware/catalog/'
		cls.items = ItmJson(
			#takes the path where json data file to be stored.
			directory_path=cls.directory_path
			)

	def test_retrieve_data(self):
		'''
		Test of creation of json directory and file(s).
		'''
		self.direct_path = Path(self.items.dir_path + 'json/')
		self.file_name = Path(self.items.dir_path + 'json/items.json')
		self.json_items = self.items.retrieve_json()

		assert self.direct_path.exists() == True
		assert self.file_name.exists() == True

	def test_json_data_saved(self):
		'''
		Test Json data file is saved and retrieved for iteration.
		'''
		self.data_retrieval = self.items.retrieve_json()

		assert 'objects' in self.data_retrieval
		assert 'category_id' in self.data_retrieval['objects'][1]['item_data']


class Test_Catalog_CategoryJson(object):
	'''
	Test CategoryJson Class
	'''
	@classmethod
	def setup_class(cls):
		cls.connect = Sq_Connect()
		cls.category = CategoryJson()
		#hard coded path of file
		cls.directory_path = '/Users/cgumbs/Devs/projects/pysqware_http/PySqware/sqware/catalog/'
		cls.items = ItmJson(
			#takes the path where json data file to be stored.
			directory_path=cls.directory_path
			)

	def test_category_dir_and_category_file_exists(self):
		self.json_dir = Path(self.directory_path + 'json/')
		self.category_file = Path(self.directory_path + 'json/category.json')

		assert self.json_dir.exists() == True
		assert self.category_file.exists() == True






