# Working with Web Data
**Refer web_data_handling.py**  
```urllib``` module is used to send request and receive response from a server. It can used to get html data
from a web page or hit an api and get data from it.  
To open a connection, ```urllib.request.url(URL)``` is used. It returns an object
 of class *http.client.HTTPResponse*
```python
import urllib.request
webUrl = urllib.request.urlopen("http://www.google.com")
```

```.getcode()``` returns the status code of the connection establishment.  
```.read()``` return the HTML data of the webpage.  

**Refer parse_json.py**
If a get type request is made on an API, it will return a response. Here ```.read()``` function will
return the json response. To parse json ```json``` module of Python is used.
```python
import json
json_data = json.loads(response)
```
Here *response* is in bytes and *json_data* is a python dictionary. Hence ```json.loads```
implicitly converts bytes to string and returns a dictionary. The response from API
can now to accessed as a normal python dictionary.

**Refer parse_html.py**
Python provides modules to parse HTML as well. 
