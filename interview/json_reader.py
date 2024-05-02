#
# Title: json_reader.py
# Description: json reader demonstration
#
import json
from typing import Dict

class Solution:

    def read_file(self, file_name: str) -> Dict[str, str]:
        buffer = {}

        try:
            with open(file_name) as infile:
                buffer = json.load(infile)
        except Exception as error:
            print(error)

        return buffer

    def execute(self, file_name: str):
        print("execute")

        buffer = self.read_file(file_name)
        print(buffer)

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.execute("json_reader.json")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
