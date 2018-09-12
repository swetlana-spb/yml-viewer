#yml-viewer
This is an app, consists of two main scripts. 
First of them uploading data from .xml file into redis database.
Second of them showing data from redis database.

#requirements
To run this app you may need:
 - python 3.x
 - PyQt5
 - redis-py
 - lxml

#uploader


usage: main_uploader.py [-h] -f FILENAME [-H HOST] [-p PORT] [-P [PASSWORD]]

Uploading data from .xml into redis database.

optional arguments:

  -h, --help            show this help message and exit
  
  -f FILENAME, --fileName FILENAME path to a file
  
  -H HOST, --host HOST  ip-address of the database
  
  -p PORT, --port PORT  port of the database
  
  -P [PASSWORD], --password [PASSWORD] password to the database
 
 Note: if you don't provide host, port or password, this script will try to connect to localhost
 
 #viewer
 
 usage: main_viewer.py [-h] [-H HOST] [-p PORT] [-P [PASSWORD]]

Shows data from redis database.

optional arguments:

  -h, --help            show this help message and exit
  
  -H HOST, --host HOST  ip-address of the database
  
  -p PORT, --port PORT  port of the database
  
  -P [PASSWORD], --password [PASSWORD] password to the database
  
Note: if you don't provide host, port or password, this script will try to connect to localhost
 