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
		cls.new_customer_3 = Sq_Customer(
			first_name = "Mike",
			last_name = "Test",
			email = "MikeTest@testing.com",
			phone = "1-123-345-1234"
			)

		cls.create_customer_3 = cls.new_customer_3.create_customer(cls.new_customer_3.custmr_data)
		

	def test_def_check_for_customer_email(self):
		'''
		Checks if customer account already exists.
		'''
		#creates new customer instance
		self.create_customer = self.customer.create_customer(self.customer.custmr_data)
		#checks for newly created customer via email
		self.customer_exists = self.customer.check_customer_email(self.customer.email)
		#error check
		self.no_customer_exists = self.customer.check_customer_email('MyName@gmail.com')

		assert self.customer_exists['email_address'] == self.customer.email
		assert self.no_customer_exists == False

	def test_create_customer(self):
		'''
		Test customer creation.
		'''
		#creates new customer from instance
		self.customer_creation = self.new_customer.create_customer(self.new_customer.custmr_data)
		#check customer exists via email.
		self.customer_check =  self.new_customer.check_customer_email(self.new_customer.email)
		
		assert self.customer_creation['customer']['given_name'] == self.new_customer.first_name
		assert self.customer_check['email_address'] == self.new_customer.email

		#delete customer
		self.new_customer.delete_customer(self.customer_check['id'])

	def test_delete_customer(self):
		'''
		Test customer deletion.
		'''
		#check is customer exists.
		self.customer_check = self.new_customer_3.check_customer_email(self.new_customer_3.email)
		#deletes account from system.
		self.delete_customer  = self.new_customer_3.delete_customer(self.customer_check['id'])
		
		assert self.customer_check['email_address'] ==  self.new_customer_3.email
		assert bool(self.delete_customer) ==  False

	def test_retrieve_customer(self):
		'''
		Test customer retrieval of data from square customer endpoint.
		'''
		#check if customer exist.
		self.customer_exists = self.customer.check_customer_email(self.customer.email)
		#retrieves customer data from square api
		self.customer_data =  self.customer.get_customer(self.customer_exists['id'])
		#error check
		self.wrong_customer = self.customer.get_customer('1PZASnAW!FSL')
		
		assert self.customer_data['customer']['id'] == self.customer_exists['id']
		assert self.wrong_customer == 'Customer not found. Please try again.'

		#deletes account from system.
		self.customer.delete_customer(self.customer_exists['id'])


	def test_update_customer_personal_information(self):
		'''
		Test customer personal information update.
		'''
		#create user instance
		self.create_customer_2 = self.new_customer_2.create_customer(self.new_customer_2.custmr_data)
		
		#update data
		self.data = {
			'given_name': 'greg',
			'email_address': 'greg@testing.com',
			'address': {
				'address_line_1': '1234 Main Street',
				'address_line_2': '',
				'locality': 'New York',
				'administrative_district_level_1': 'NY',
				'postal_code': '11413',
				'country': 'US'
			}
		}

		#check and retrieve customer data via original email
		self.get_customer = self.new_customer_2.check_customer_email(self.new_customer_2.email)
		#updates new data to account.
		self.update_customer = self.new_customer_2.update_customer_acct(self.get_customer['id'], self.data)
		#check if email is updated on account.
		self.check_updates = self.new_customer_2.check_customer_email(self.update_customer['customer']['email_address'])

		assert self.update_customer['customer']['given_name'] == self.data['given_name']
		assert self.update_customer['customer']['address']['address_line_1'] == self.data['address']['address_line_1']
		assert self.check_updates['email_address'] ==  self.update_customer['customer']['email_address']
		assert self.update_customer['customer']['email_address'] == self.data['email_address']
		
		#deletes account from system.
		self.new_customer_2 .delete_customer(self.get_customer['id'])

	def test_update_customer_email(self):
		'''
		Test customer email update.
		'''
		#customer data
		self.customer = Sq_Customer(
			first_name = 'John',
			last_name = 'Doe',
			email = 'John_D@johndoe.com',
			phone= '123-456-7890'
			)

		#creates customer
		self.customer.create_customer(self.customer.custmr_data)

		#new email data
		self.data = {
		'email_address': 'new_address@testing.com'
		}

		#check new customer email and retrieve customer data
		self.get_customer = self.customer.check_customer_email(self.customer.email)
		#use customer ID to update email
		self.update_email =  self.customer.update_customer_email(self.get_customer['id'], self.data)
		#check if email is updated
		self.updated_email =  self.customer.check_customer_email(self.data['email_address'])

		assert self.get_customer['id'] ==  self.updated_email['id']
		assert self.update_email['customer']['email_address'] ==  self.data['email_address']
		assert self.updated_email['email_address'] == self.data['email_address']

		#deletes account from system.
		self.customer.delete_customer(self.get_customer['id'])