#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Retrieve Categories, search for items in category, and returns items.

'''

import json
import requests
from .connections import Sq_Connect


class Sq_Catalog(object):
	def __init__(self):
		self.connect = Sq_Connect()