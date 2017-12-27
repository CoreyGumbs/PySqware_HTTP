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
from sqware.connect import Sq_Connect
from sqware.catalog import get_categories

#Test of Sq_Connect Catagories Functionality
class Test_Sq_Connect_Catalog(object):
	'''
	Testing of the Sq_connect catagories functionality. Currently uses the square sandbox application ID and Access Token.

	'''
	@classmethod
	def setup_class(cls):
		#create class instance of Sq_Connect
		cls.connect = Sq_Connect()

	def test_catalog_categories_retrieval(self):
		'''
		Test for the retrieval of catalog categories.
		'''
		#uses location id from Sq_Connect() location_id variable.
		#returns list of json data for individual store location.
		catalog = get_categories(self.connect.location_id)
		
		#Retrieve category name
		assert catalog[0]['name'] == 'Smoothies'
		#Retrieve category ID
		assert catalog[2]['id'] == 'X5VKXVI6I2ZPBFF75YTDNNL2'









