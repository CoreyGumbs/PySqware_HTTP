#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Retrieve individual store Categories.

'''
import json
import requests
from sqware.connect import Sq_Connect
from sqware.catalog import get_categories


class Sq_Products(object):
	'''
	'''
	def __init__(self):
		'''
		'''
		self.connect = Sq_Connect()
		self.location_id = self.connect.location_id

	


		