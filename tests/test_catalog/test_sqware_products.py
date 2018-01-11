	#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the Sqware package Sq_Products Class.
'''
import pytest
from sqware.catalog import get_categories, Sq_Products

class Test_Catalog_Products(object):
	'''
	Test of Sq_Products Class.
	'''
	@classmethod
	def setup_class(cls):
		cls.products = Sq_Products()
		cls.category = get_categories()


	def test_get_product_items(self):
		'''
		Retrieve products associated with an item
		'''
		#selected category_id
		self.cat_id = self.category[2]['id']
		#calls to find products associated with category_id
		self.cat_items = self.products.get_category_items(self.cat_id)
		print(len(self.cat_items))

		assert 'X5VKXVI6I2ZPBFF75YTDNNL2' in self.cat_items[0]['item_data']['category_id']
		assert 'X5VKXVI6I2ZPBFF75YTDNNL2' in self.cat_items[1]['item_data']['category_id']
		assert 'X5VKXVI6I2ZPBFF75YTDNNL2' in self.cat_items[2]['item_data']['category_id']
		assert 'X5VKXVI6I2ZPBFF75YTDNNL2' in self.cat_items[3]['item_data']['category_id']
		




		

