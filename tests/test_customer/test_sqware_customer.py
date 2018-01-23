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

		assert self.customer_exists['email_address'] == self.customer.email
		assert self.no_customer_exists == False

	def test_retrieve_customer(self):
		'''
		Test customer retrieval of data from square customer endpoint.
		'''

		self.customer_exists = self.customer.check_customer(self.customer.email)
		self.customer_data =  self.customer.get_customer(self.customer_exists['id'])
		self.wrong_customer = self.customer.get_customer('1PZASnAW!FSL')
		
		assert self.customer_data['customer']['id'] == self.customer_exists['id']
		assert self.wrong_customer == 'Customer not found. Please try again.'

	def test_create_customer(self):
		'''
		Test customer creation
		'''
		self.new_customer = Sq_Customer(
			first_name = "John",
			last_name = "Times",
			email = "tim@testing.com",
			phone = "1-123-345-1234"
			)
		self.customer_creation = self.new_customer.create_customer(self.new_customer.custmr_data)
		self.customer_check =  self.new_customer.check_customer(self.new_customer.email)

		assert self.customer_creation['given_name'] == self.new_customer.first_name
		assert self.customer_check['email_address'] == self.new_customer.email
