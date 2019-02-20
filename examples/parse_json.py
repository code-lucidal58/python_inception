import json
import urllib.request


def print_results(data):
    json_data = json.loads(data)
    if "title" in json_data["metadata"]:
        print(json_data["metadata"]["title"])
    count = json_data["metadata"]["count"]
    print(count, "events recorded")
    for i in json_data["features"]:
        print(i["properties"]["place"])
    for i in json_data["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])


def main():
    url_data = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    web_url = urllib.request.urlopen(url_data)
    print("result code:", str(web_url.getcode()))
    if web_url.getcode() == 200:
        data = web_url.read()
        print_results(data)
    else:
        print("Received error, cannot parse results")


if __name__ == "__main__":
    main()
