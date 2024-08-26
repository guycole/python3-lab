#
# Title: driver.py
# Description: 
# 
#

class Driver:

  def __init__(self):
    self.dd = {}

  # convert from decimal degrees
  def dd_key(self, rawbuff:str) -> str:
    tokens = rawbuff.split('.')

    element1 = tokens[1][0:2]
    element2 = tokens[1][2:4]

    result = f"{tokens[0]}_{element1}_{element2}"
    return result

  def parser(self, rawbuff:str):
    tokens = rawbuff.strip().split(' ')
    if len(tokens) != 2:
      print("fail")

    key_lat = self.dd_key(tokens[0])
    key_lng = self.dd_key(tokens[1])

    fresh_key = f"{key_lat}/{key_lng}"

    self.dd[fresh_key] = (tokens[0], tokens[1])

  def execute(self, file_name: str) -> None:
    print("execute")

    try:
      with open(file_name, 'r') as infile:
        buffer = infile.readlines()
        for element in buffer:
          self.parser(element)
    except Exception as error:
      print(error)

    print(self.dd)

if __name__ == '__main__':
  print("main")

  driver = Driver()
  driver.execute("file1.dat")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
