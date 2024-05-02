#
# Title:urllib.py
# Description: urllib demo
#
# https://realpython.com/python-requests/
#
#import urllib.request
import requests

class Main:

    def execute(self):
        response = requests.get("https://api.github.com")
        #print(response.text)
        json_dict = response.json()
        print(json_dict)
        print(response.headers)

        response = requests.get(
          "https://api.github.com/search/repositories", params={"q": "language:python", "sort": "stars", "order": "desc"},)
        print(response)



#        contents = urllib.request.urlopen("http://www.yahoo.com").read()
#        print(contents)

#        with urllib.request.urlopen('http://www.python.org/') as f:
#            print(f.read(100).decode('utf-8'))

#
# main driver
#
if __name__ == '__main__':
    driver = Main()
    driver.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
