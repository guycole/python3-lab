#
# Title:urllib.py
# Description: urllib demo
#
import urllib.request

class Main:

    def execute(self):
        contents = urllib.request.urlopen("http://www.yahoo.com").read()
        print(contents)

        with urllib.request.urlopen('http://www.python.org/') as f:
            print(f.read(100).decode('utf-8'))

#
# main driver
#
if __name__ == '__main__':
    driver = Main()
    driver.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
