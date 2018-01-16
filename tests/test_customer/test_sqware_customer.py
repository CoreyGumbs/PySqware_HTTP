	#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the Sqware package Sq_Customers Class.
'''
import pytest
from sqware.connect import Sq_Connect
from sqware.customer import Sq_Customer

class Test_Customer(object):
	'''
	'''
	@classmethod
	def setup_class(cls):
		cls.connect = Sq_Connect()
		cls.customer = Sq_Customer(
			first_name = 'Testy',
			last_name = 'McTesty',
			email = 'McTesty@testy.com',
			phone= '123-456-7890'
			)

	def test_def_check_for_customer(self):
		'''
		Checks if customer account already exists.
		'''
		self.customer_exists = self.customer.check_customer(self.customer.email)
		self.no_customer_exists = self.customer.check_customer('MyName@gmail.com')

		assert self.customer_exists == True
		assert self.no_customer_exists == False