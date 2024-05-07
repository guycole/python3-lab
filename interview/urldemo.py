#
# Title:urldemo.py
# Description: urldemo
# https://realpython.com/python-requests/
#
import json
import requests
from requests.auth import HTTPBasicAuth

class Main:

    def execute(self):
        response = requests.get("https://api.github.com")
        #print(response.text)
        json_dict = response.json()
        #print(json_dict)
        #print(response.headers)

        response = requests.get("https://api.github.com/search/repositories", params={"q": "language:python", "sort": "stars", "order": "desc"},)
        print(response)
        print(response.json())

        response = requests.post("https://httpbin.org/post", data={"key": "value"}) 
        print(response)
        print(response.json())


        response = requests.get("http://localhost:8080/api/simple/", auth=HTTPBasicAuth("admin", "byteme"))
        print(response)
        print(response.json())

        response = requests.post("http://localhost:8080/api/simple/", auth=HTTPBasicAuth("admin", "byteme"), data={"key": "zzz", "value": "yyy"}) 
        print(response)
        print(response.json())

#
# main driver
#
if __name__ == '__main__':
    driver = Main()
    driver.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***