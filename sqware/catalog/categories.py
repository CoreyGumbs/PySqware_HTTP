#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Retrieve individual store Categories.

'''
from sqware.catalog import CategoryJson 

def get_categories():
	'''
	Retrieves categories from json file.
	'''
	#enter path where json directory is located.
	categories = CategoryJson()
	return categories.retrieve_json()