#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Establishes Connection to Square API to allow access to store data for manipulation.

'''

import os
import json
import requests
import squareconnect
from sqware.connect.secrets import get_secrets


class Sq_Connect(object):
	def __init__(self):
		'''constructor for class'''
		self.access_token = get_secrets('ACCESS_TOKEN')
		self.application_id = get_secrets('APPLICATION_ID')
		#If multiple locations needed, add multiplelocation_id via incriments on secrets.json 
		#(IE: location_id_2 = {{square location 2 ID}})
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
			if sq_connection.status_code == requests.codes.ok:
				return sq_connection
			else:
				return sq_connection.raise_for_status()
		except requests.exceptions.HTTPError as errhttp:
			return str(errhttp)
		except requests.exceptions.ConnectionError as errconn:
			return '{}{}'('Error Connecting: ', errconn)
		except requests.exceptions.Timeout as errto:
			return '{}{}'.format('Timeout Error: ',errto)
		except requests.exceptions.RequestException as err:
			return '{}{}'.format("Other Error: ", err)

	
	def post(self, request_path, data):
		'''
		Posts to Square API.
		Must include data parameter accepts json dictionaries.
		'''
		sq_connection = requests.post('https://connect.squareup.com' + request_path, headers = self.request_headers, json=data)
		try: 
			if sq_connection.status_code == requests.codes.ok:
				return sq_connection
			else:
				return sq_connection.raise_for_status()	
		except requests.exceptions.HTTPError as errhttp:
			return str(errhttp)
		except requests.exceptions.ConnectionError as errconn:
			return '{}{}'('Error Connecting: ', errconn)
		except requests.exceptions.Timeout as errto:
			return '{}{}'.format('Timeout Error: ',errto)
		except requests.exceptions.RequestException as err:
			return '{}{}'.format("Other Error: ", err)




