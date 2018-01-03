#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
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
		return '{}'.format('Square API Json Data')

	def __get_item_json(self):
		'''
		Retrieves JSON data for all items/products in square catalog. 
		'''
		#gets data from square catalog endpoint
		self.get_data = self.connect.get('/v2/catalog/list?types=item')
		#decodes json data
		self.retrieved_data = self.get_data.json()
		self.json_data = json.dumps(self.retrieved_data, sort_keys=True, indent=4)

		return self.json_data

	def __directory_check(self, path_name):
		'''
		Checks if directory exists. If it doesn't creates directory in user supplied path.
		'''
		#set directory path
		dir_name = Path(path_name)
		#tests if directory exists. creates new one if it doesnt.
		while not dir_name.exists():
			dir_name.mkdir(parents=True, exist_ok=False)
		else:
			return dir_name.exists()

	def __write_item_json(self, path_name, json_data):
		self.directory = self.__directory_check(self.dir_path)
		self.file_name = Path(str(path_name +'/items.json'))
		print(self.directory)
		if self.directory:
			if not self.file_name.exists():
				print('doesnt exist')
			else:
				return self.file_name.exists()


	def get_data(self):
		return self.__write_item_json(self.dir_path ,self.__get_item_json())

 



