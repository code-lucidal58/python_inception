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
## JSON Parsing
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

## HTML Parsing
**Refer parse_html.py**
Python provides class to parse HTML as well. Custom HTMLParser is developed to override methods and performs
required tasks.
```python
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass
        
parser = MyHTMLParser()
f = open("sample.html")
if f.mode == 'r':  # file successfully opened
    contents = f.read()
    parser.feed(contents)

```
```error``` is an abstract method of ```HTMLParser``` class. There are other methods that can be overridden
to add required functionality, like ```handleComment```, ```HandleStartTag```, ```HandelData```, etc. 

## XML Parsing
**Refer parse_xml.py**
Sometimes it is required to operate on the document as whole
by storing it in the memory, rather than reading it line by line. This is required
when manipulations and operations are to be performed repetitively and at will. For this, 
operate on the DOM. While working .xml file, ```xml.dom.minidom``` can be used to store the
document in the memory.
```python
import xml.dom.minidom
doc = xml.dom.minidom.parse("sample.xml")
```
Here ```doc``` is an object of type **xml.dom.minidom.Document**. In the dom element, each tag is a node. An nodes 
have children. Using this object, data can be manipulated or read. Any changes made to this document will not be
reflected to the xml file.

[Next](./part_7_oop_1.md)  
[Back](/README.md)
