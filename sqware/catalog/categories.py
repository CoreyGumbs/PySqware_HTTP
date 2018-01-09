#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Retrieve individual store Categories.

'''
import json
import requests
from sqware.catalog import ItmJson, CategoryJson 

def get_categories():
	'''
	Retrieves categories from json file.
	'''
	#enter path where json directory is located.
	categories = CategoryJson()
	return categories.retrieve_json()