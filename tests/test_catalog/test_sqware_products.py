	#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the Sqware package Sq_Products Class.
'''
import pytest
from pathlib import Path
from sqware.connect import Sq_Connect
from sqware.catalog import get_categories 

class Test_Catalog_Products(object):
	'''
	'''
	@classmethod
	def setup_class(cls):
		cls.connect = Sq_Connect()
		cls.categories = get_categories()


	def test_get_product_items(self):
		'''
		'''
		pass



		

