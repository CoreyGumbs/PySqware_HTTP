	#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the Sqware package Sq_Products Class.
'''
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



		

