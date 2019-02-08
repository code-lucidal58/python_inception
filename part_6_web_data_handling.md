# Working with Web Data
```urllib``` module is used to send request and receive response from a server. 
```python
import urllib.request

webUrl = urllib.request.urlopen("http://www.google.com")
print("result code:", webUrl.getcode()) # 200
data = webUrl.read()
print(data) # prints HTML for the page
```