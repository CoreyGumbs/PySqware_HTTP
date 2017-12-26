#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the SqWare package Sq_Connect Class.
'''
import os
import pytest
import requests 
import json
import timeit
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
		catalog = self.sq_category.connect_catalog('/v2/catalog/list')
	
		assert catalog.status_code == requests.codes.ok
		assert catalog.url == 'https://connect.squareup.com/v2/catalog/list'

	def test_catalog_categories_retrieval(self):
		'''
		Test for the retrieval of catalog id.
		'''
		#catalog class instance
		#self.sq_category.location  calls the location_id that inherits from the Sq_Connect class constructor.
		catalog = self.sq_category.get_categories(self.sq_category.location)
		
		assert catalog[0]['name'] == 'Smoothies'
		assert catalog[2]['id'] == 'X5VKXVI6I2ZPBFF75YTDNNL2'

	def test_catalog_categories_items_retrieval(self):
		'''
		Test catalog_id filters through json data to retrieve items associated with the id.
		'''
		#catalog class instance
		catalog = self.sq_category.get_categories(self.sq_category.location)
		#uses catalog id to retrieve items associated with it.
		catalog_item = self.sq_category.get_cat_items(catalog[2]['id'], catalog[2]['name'])
		catalog_item_error = self.sq_category.get_cat_items('1EdSJSNRTKSSH')

		#test category id matches products category ids.
		assert catalog[2]['id'] == catalog_item[1]['item_data']['category_id']

		#test list item ids.
		#assert catalog_item[0]['name'] == ''
		assert catalog_item[0]['id'] == 'LSRV7KDOIE4YNS3DMSDS5Y6C'
		assert catalog_item[2]['id'] != 'VM7HX7V7ZZPHYUJPDTD2KC7N'

		#test how deep information can be retrieved.
		assert catalog_item[0]['item_data']['variations'][0]['item_variation_data']['price_money']['amount'] == 999

		#test wrong ID entered.
		assert catalog_item_error == None

	def test_catalog_categories_items_retrieval_file_and_directories(self):
		'''
		'''
		#catalog class instance
		catalog = self.sq_category.get_categories(self.sq_category.location)
		#uses catalog id to retrieve items associated with it.
		catalog_item = self.sq_category.get_cat_items(catalog[2]['id'], catalog[2]['name'])

		#test category id matches products category ids.
		assert catalog[2]['id'] == catalog_item[1]['item_data']['category_id']

		#check directory exists
		assert os.path.exists('../sqware/item_json') == True
		assert os.path.isdir('../sqware/item_json') == True







