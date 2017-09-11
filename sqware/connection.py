#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Establishes Connection to Square API to allow access to store data for manipulation.

'''

import os
import json
from http import client

#Globals for connecting to Sqaure API
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCESS_TOKEN = 'sandbox-sq0atb-klNxv-KKF1pq1He5DzJ-Lg'

class Sq_Connect(object):
	def __init__(self):
		'''constructor for class'''
		self.access_token = ACCESS_TOKEN

	def establish(self):
		return self.access_token