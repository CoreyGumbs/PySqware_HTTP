# PySqware
A simple module for the Django Framework to use with the Square API. 

Rather than having to upload products into two seperate systems, users can use this program to 
update web applications in real time as changes are madeto square accounts (IE: products, categories, etc.).

Any changes made to the Square Dashboard or POS system will reflect on the web application in real time. 

This program assumes that you have already set-up a square merchant accounts and have access to 
the following square credentials:

+ Access Token
+ Application ID 
+ Location(s) ID


Version 0.3.0
-------------

written using Python 3

#### New Feature(s):
+ Added Customer module - CRUD module with sq_customer class for customers (create customer, check email, update customer, update email, delete account.)

#### Previous Feature(s):
+ Added catalog module - catalog module collects and creates json data of categories and items from API. It also has a product module that allows items associated with a category_id to be returned for data manipulation.
+ Added Sq_Connect class with a connect_api function for connection to Square api.


Connect
-------
The Connect class

#### License:

This project is licensed under the MIT License.