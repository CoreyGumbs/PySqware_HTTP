#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test of the SqWare package Sq_Connect Class.
'''

import pytest
from sqware.connection import Sq_Connect

#Test of Sq_Connect Module
class Test_Sq_Connect(object):
	'''
	Testing of the Sq_connect module. Currently uses the square sandbox application ID and Access Token.

	'''

	@classmethod
	def setup_class(cls):
		cls.sq_connect = Sq_Connect()

	def test_establish_connection(self):
		'''
		Test the connection to square api for user account.
		Change  access_token to either sandbox or production access_token
		'''
		access_token = 'sandbox-sq0atb-klNxv-KKF1pq1He5DzJ-Lg'

		assert self.sq_connect.establish() == access_token



	


 