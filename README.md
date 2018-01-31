# PySqware
A simple package that connects web applications to a Square Account via API that takes and processes web based orders via a personal/business site. It also automatically updates store products/service changes made through the Square POS, app, or website.

Version 0.3.0
-------------

written using Python 3

#### New Additions(s):
+ Added Customer module - CRUD module with sq_customer class for customers (create customer, check email, update customer, update email, delete account.)

#### Previous Addition(s):
+ Added catalog module - catalog module collects and creates json data of categories and items from API. It also has a product module that allows items associated with a category_id to be returned for data manipulation.
+ Added Sq_Connect class with a connect_api function for connection to Square api.

