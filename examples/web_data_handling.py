import urllib.request

def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code:", webUrl.getcode())
    data = webUrl.read()
    print(data) # prints HTML for the page

if __name__ == "__main__":
    main()