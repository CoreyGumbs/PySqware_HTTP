#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Establishes Connection to Square API to allow access to store data for manipulation.

'''

import os
import json
import requests
import squareconnect
from sqware.secrets import get_secrets


class Sq_Connect(object):
	def __init__(self):
		'''constructor for class'''
		self.access_token = get_secrets('ACCESS_TOKEN')
		self.application_id = get_secrets('APPLICATION_ID')
		#If multiple locations needed, add multiplelocation_id via incriments on secrets.json 
		#(IE: location_id_2 = {{square location ID}})
		self.location_id = get_secrets('LOCATION_ID')
		self.request_headers = {
			'Authorization': 'Bearer ' + self.access_token,
			'Accept':        'application/json',
			'Content-Type':  'application/json'
			}

	def get(self, request_path):
		'''
		Connects user to square api. 
		User adds endpoint path as per Square API documentation.
		ex: sq_connect.get('/v2/locations')
		'''

		#create connection to Square API using Requests library.
		#Uses custom header parameter to pass  requireed square api headers.
		#'timeout' parameter can be changed to desired time. See Requests docs (http://docs.python-requests.org/en/master/user/quickstart/#custom-headers).
		sq_connection = requests.get('https://connect.squareup.com' + request_path, headers = self.request_headers, timeout=3)
		try:
			sq_connection.raise_for_status()
			return sq_connection	
		except requests.exceptions.RequestException as e:
			return str(e)

	
	def post(self, request_path, data):
		'''
		Posts to Square API.
		Must data parameter accepts json dictionaries.
		'''
		sq_connection = requests.post('https://connect.squareup.com' + request_path, headers = self.request_headers, json=data)
		try: 
			sq_connection.raise_for_status()
			return sq_connection	
		except requests.exceptions.RequestException as e:
			return str(e)




