# PySqware
A simple module for the Django Framework to use with the Square API. 

Rather than having to upload products into two seperate systems (DJango Admin/Square POS), users can use this program to 
update web applications as changes are made to square (IE: products, categories, etc.) via the Square dashboard or POS.

Square Business/Merchant Account needed before using.


## Version 0.3.0

written using Python 3


## Features

#### Recently Added Feature(s):
+ Added Customer module - CRUD module with sq_customer class for customers (create customer, check email, update customer, update email, delete account.)

#### Previously Added Feature(s):
+ Added catalog module - catalog module collects and creates json data of categories and items from API. It also has a product module that allows items associated with a category_id to be returned for data manipulation.
+ Added Sq_Connect class with a connect_api function for connection to Square api.



## Connect - Secrets.py and Secrets.json


#### Read First

If you have not created a square business account, please do so before continuing.
The Connect class assumes that you have already set-up a square merchant account and have access to 
the following square credentials:

+ Access Token
+ Application ID 
+ Location(s) ID

#### Secrets.py and Secrets.json
Before you are able to use the Square API or Sq_Connect class, you have to first create your secrets.json file to use with the secrets.py file.
Rather than hard coding your Access Token, Application ID, and Location ID headers everytime you send a request, these two files ensure that you only have
to set-up once as well as protect your sensitive data.

##### Secrets.py
There are two global variables : **BASE_DIR and  SECURITY KEY**

```python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECURITY_KEY = os.path.join(BASE_DIR, 'secrets.json')
```

They are currently set to the **connect** module file path. You can change the file path to your desired path.

Just remember to assign the **SECURITY_KEY** file path to where you will be storing your secrets.json file.

To use the **get_secrets()** refer below


#### Secrets.json 
This is the json file is where you will store all sensitive data used for the Square API headers, module file storage directories, etc.

**Sample Structure**
```json
{
	"ACCESS_TOKEN": "[square access token goes here.]",
	"APPLICATION_ID": "[square application id goes here.]",
	"LOCATION_ID": "[square store location goes here.]",
}
```
**Note:** You may have more than one location you are using. Just create a new key such as "LOCATION_ID_2" : "value" 

#### get_secrets(setting) method from Secrets.py

This method is used to parse the secrets.json file, retrieve desired setting, and returns value from json file.

To access your settings from the secrets.json file, you can import and use the get_secrets() method found on secrets.py.

This example uses the json sample from above.

```python
from sqware.connect.secrets import get_secrets

ACCESS_TOKEN = get_secrets('ACCESS_TOKEN') 
LOCATION_ID = get_secrets('LOCATION_ID')

```

This will return the value of that setting to be used in headers, or other methods that may require sensitive data. 
You will see a working example with the Sq_Connect class.

## Connect - Connection.py

#### Endpoints

The Sq_Connect class utilizes the **GET, POST, PUT, DELETE** http methods through the Requests library. These methods conincide with the 
CRUD endpoints of the Square API: [Endpoint Names and Return Values](https://docs.connect.squareup.com/api/connect/v2#endpointnamesandreturnvalues "Endpoint Names and Return Values"). 

#### Sensitive Data Handling - Square Access Token and Application ID

In order to send data to the Square API, it requires a header that passes the square access token: [Get Started with Square](https://docs.connect.squareup.com/articles/getting-started "Getting Started").

Without this header, all requests will return errors.

To prevent this, the Sq_Connect class is set up to recieve all data from your secrets.json file via the get_secrets method.

You can find the variables within the __init__ constructor method.

```python
def __init__(self):
		'''constructor for class'''
		self.access_token = get_secrets('ACCESS_TOKEN')
		self.request_headers = {
			'Authorization': 'Bearer ' + self.access_token,
			'Accept':        'application/json',
			'Content-Type':  'application/json'
			}
```

**Note:** You may decided to change your json setting keys on the secrets.json file. If you do that make sure you update those setting keys within the __init__ method or an error will return.

```python
def __init__(self):
		'''constructor for class'''
		self.access_token = get_secrets('CHANGED_KEY')
```

----

#### Sq_Connect Instance

In order to call the necessary http methods, an instance of Sq_Connect is needed.

```python
from sqware.connect import Sq_Connect

self.connect = Sq_Connect()
```

Once an instance is set, we can call the neccessary http method needed. 

-----

##### Sq_Connect: GET/DELETE methods

The **GET/DELETE** http methods only require the path to the requested Square API endpoint(s). 

The Sq_Connect.get() method 

See example.

**Example**

```python
from sqware.connect import Sq_Connect

self.connect = Sq_Connect()

self.connect.get(endpoint_path)

or

self.connect.get('/v2/locations')
```

In this example, this will return a json response object of all locations associated with the Square account. See the [Square API Documentation](https://docs.connect.squareup.com/api/connect/v2#navsection-locations) for more information about their endpoints. 

## License:


This project is licensed under the MIT License.