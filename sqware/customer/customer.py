#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqware.connect import Sq_Connect


class Sq_Customer(object):
	'''
	'''
	def __init__(self, first_name, last_name, email, phone):
		'''x
		'''
		self.connect =  Sq_Connect()
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone = phone

	def __str__(self):
		pass


	def check_customer(self, email):
		'''
		Checks if customer already exists in square.
		'''
		pass