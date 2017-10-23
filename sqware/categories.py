#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Retrieve Categories, search for items in category, and returns items.

'''

import json
import requests
from sqware.connection import Sq_Connect


class Sq_Catalog(object):
	def __init__(self):
		self.connection = Sq_Connect()


	def retrieve_catalog_categories(self, request_path):
		catalog_endpoint = self.connection.connect_api(request_path)
		catalog_data = catalog_endpoint.json()
		data = [item for item in catalog_data['objects'] if 'catalog_data' in item]
		return catalog_data