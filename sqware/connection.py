#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Establishes Connection to Square API to allow access to store data for manipulation.

'''

import os
import json
import http.client as httplib
import squareconnect
from sqware.secrets import get_secrets


class Sq_Connect(object):
	def __init__(self):
		'''constructor for class'''
		self.access_token = get_secrets('ACCESS_TOKEN')
		self.application_id = get_secrets('APPLICATION_ID')
		self.location_id = get_secrets('LOCATION_ID')
		self.request_headers = {
			'Authorization': 'Bearer ' + self.access_token,
			'Accept':        'application/json',
			'Content-Type':  'application/json'
			}

	def connect_api(self, request_path):
		conn = httplib	.HTTPSConnection('connect.squareup.com')
		conn.request('GET', request_path, '', self.request_headers)
		response = conn.getresponse()
		data = json.loads(response.read())
		return json.dumps(data, indent=2, separators=(',',': '))

	

a = Sq_Connect()

a.connect_api('/v2/catalog/object/')




