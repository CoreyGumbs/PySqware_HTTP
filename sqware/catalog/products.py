#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Retrieve individual store Categories.

'''
import json
import requests
from pathlib import Path
from sqware.connect import Sq_Connect



class Sq_Products(object):
	'''
	'''
	def __init__(self):
		'''
		'''
		self.connect = Sq_Connect()
		self.location_id = self.connect.location_id

	


		