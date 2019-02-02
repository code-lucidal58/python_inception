import urllib.request


def main():
    web_url = urllib.request.urlopen("http://www.google.com")
    print("result code:", web_url.getcode())
    print(type(web_url))
    data = web_url.read()
    print(data)  # prints HTML for the page


if __name__ == "__main__":
    main()
