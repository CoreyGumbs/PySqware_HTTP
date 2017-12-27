#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Retrieve individual store Categories.

'''
import os
import json
import requests
from sqware.connect import Sq_Connect

def get_categories(location_id):
	'''
	Retrieves category from individual square location.
	'''
	#Sq_Connect instance
	connect = Sq_Connect()
	#Connect to square api using location_id
	category_endpoint = connect.get('/v1/' + location_id + '/categories')
	#Decodes json data as list
	category_data= category_endpoint.json()
	return category_data