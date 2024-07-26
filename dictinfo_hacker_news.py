#See what key values available in this API call
import json
import requests

url = "https://hacker-news.firebaseio.com/v0/item/41069829.json"
r = requests.get(url)
print(f"Status code:{r.status_code}")
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)