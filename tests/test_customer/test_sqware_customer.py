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
		cls.new_customer = Sq_Customer(
			first_name = "John",
			last_name = "Times",
			email = "tim@testing.com",
			phone = "1-123-345-1234"
			)
		cls.new_customer_2 = Sq_Customer(
			first_name = "Charles",
			last_name = "Smith",
			email = "Csmith@testing.com",
			phone = "1-123-345-1234"
			)
		cls.create_customer = cls.customer.create_customer(cls.customer.custmr_data)

	def test_def_check_for_customer_email(self):
		'''
		Checks if customer account already exists.
		'''
		self.customer_exists = self.customer.check_customer_email(self.customer.email)
		self.no_customer_exists = self.customer.check_customer_email('MyName@gmail.com')

		assert self.customer_exists['email_address'] == self.customer.email
		assert self.no_customer_exists == False

	def test_create_customer(self):
		'''
		Test customer creation.
		'''

		self.customer_creation = self.new_customer.create_customer(self.new_customer.custmr_data)
		self.customer_check =  self.new_customer.check_customer_email(self.new_customer.email)

		assert self.customer_creation['customer']['given_name'] == self.new_customer.first_name
		assert self.customer_check['email_address'] == self.new_customer.email

	# def test_retrieve_customer(self):
	# 	'''
	# 	Test customer retrieval of data from square customer endpoint.
	# 	'''

	# 	self.customer_exists = self.customer.check_customer(self.customer.email)
	# 	self.customer_data =  self.customer.get_customer(self.customer_exists['id'])
	# 	self.wrong_customer = self.customer.get_customer('1PZASnAW!FSL')
		
	# 	assert self.customer_data['customer']['id'] == self.customer_exists['id']
	# 	assert self.wrong_customer == 'Customer not found. Please try again.'


	# def test_update_customer(self):
	# 	'''
	# 	Test customer update.
	# 	'''
	# 	self.data = {
	# 		'given_name': 'James',
	# 		'email_address': 'mike@testing.com',
	# 		'address': {
	# 			'address_line_1': '1234 Main Street',
	# 			'address_line_2': '',
	# 			'locality': 'New York',
	# 			'administrative_district_level_1': 'NY',
	# 			'postal_code': '11413',
	# 			'country': 'US'
	# 		}
	# 	}
	# 	self.create_customer_2 = self.new_customer_2.create_customer(self.new_customer_2.custmr_data)
	# 	self.get_customer = self.customer.check_customer(self.new_customer_2.email)
	# 	self.update_customer = self.new_customer_2.update_customer_acct(self.get_customer['id'], self.data)
	# 	#self.updated = self.customer.check_customer(self.update_customer['customer']['email_address']) 

	# 	print(self.update_customer)
	# # 	assert self.update_customer['given_name'] == self.data['given_name']
	# # 	assert self.update_cusomer['address'] == self.data['address']['address_line_1']
	# # 	assert self.updated['email_address'] == self.data['email_address']
