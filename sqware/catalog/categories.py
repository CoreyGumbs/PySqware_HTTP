#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Retrieve individual store Categories.

'''
import json
import requests
from sqware.catalog import CategoryJson 

def get_categories():
	'''
	Retrieves categories from json file.
	'''
	categories = CategoryJson(directory_path='/Users/cgumbs/Devs/projects/pysqware_http/PySqware/sqware/catalog/')
	return categories.retrieve_json()