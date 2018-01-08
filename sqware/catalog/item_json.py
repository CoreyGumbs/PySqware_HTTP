#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import json
import requests
from pathlib import Path
from sqware.connect import Sq_Connect
from sqware.catalog import get_categories


class ItmJson(object):
	'''
	Item json data
	'''
	def __init__(self, directory_path):
		self.connect = Sq_Connect()
		self.categories = get_categories(self.connect.location_id)
		self.dir_path = directory_path

	def __str__(self):
		return '{}'.format(self.dir_path)

	def __get_item_json(self):
		'''
		Retrieves JSON data for all items/products in square catalog. 
		'''
		#gets data from square catalog endpoint
		self.get_data = self.connect.get('/v2/catalog/list?types=item')
		#decodes json data
		self.retrieved_data = self.get_data.json()
		#prettifies json data
		self.json_data = json.dumps(self.retrieved_data, sort_keys=True, indent=4)
		return self.json_data

	def __directory_check(self):
		'''
		Checks if directory exists. If it doesn't creates directory in user supplied path.
		Creates a new directory if none exist. 

		*** mkdir flag - "exist_ok=False" prevents additional directories from being created. see documentation ***
		'''
		#set directory path
		dir_name = Path(self.dir_path + 'json')
		#tests if directory exists. creates new one if it doesnt.
		while not dir_name.exists():
			
			dir_name.mkdir(parents=True, exist_ok=False)
		else:
			return dir_name.exists()

	def __write_item_json(self, path_name, json_data):
		'''
		Checks if there is a json file exists.
		Creates file if none exists.
		Will overwrite any files that exists.

		*** May add a test for last time file modified and if any changes occured. ***
		'''
		self.directory = self.__directory_check()
		self.file_name = Path(str(path_name +'json/items.json'))
		#if directory exists.
		if self.directory:
			#creates file if none.
			while not self.file_name.exists():
				with open(self.file_name, 'w') as file:
					file.write(json_data)
			#overwrites file if exists.
		elif self.file_name.exists():
			with open(self.file_name, 'w') as file:
				file.write(json_data)


	def get_data(self):
		self.__write_item_json(self.dir_path ,self.__get_item_json())

 



