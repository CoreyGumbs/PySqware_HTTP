#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Establishes Connection to Square API to allow access to store data for manipulation.

'''

import os
import json
import requests
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
		#create connection to Square API using Requests library
		#Uses custom header parameter to pass  requireed square api headers
		sq_connection = requests.get('https://connect.squareup.com' + request_path, headers = self.request_headers)

		#returns request opject
		return sq_connection

	

a = Sq_Connect()

print(a.connect_api('/v2/locations'))




