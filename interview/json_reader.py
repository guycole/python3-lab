#
# Title: json_reader.py
# Description: json reader demonstration
#
# https://builtin.com/software-engineering-perspectives/python-json-schema
#
import json

from jsonschema import validate

from typing import Dict

schema = {
    "type": "object",

    "properties": {
        "project": {"type": "string"},
        "version": {"type": "number"},
        "wiFi": {
            "type": "array",
            "items": {
                "bssid": {"type": "string"},
                "ssid": {"type": "string"},
                "level": {"type": "number"},
                "frequency": {"type": "number"},
                "capability": {"type": "string"},
            }   
        },
        "geoLoc": {
            "type": "object",
            "properties": {
                "fixTimeMs": {"type": "number"},
                "provider": {"type": "string"},
                "longitude": {"type": "number"},
                "latitude": {"type": "number"},
                "accuracy": {"type": "number"},
                "altitude": {"type": "number"}
            }
        }
    },

    "required": ["project", "version"],
    "additionalProperties": False
}

class Solution:

    def read_file(self, file_name: str) -> Dict[str, str]:
        buffer = {}

        try:
            with open(file_name) as infile:
                buffer = json.load(infile)
        except Exception as error:
            print(error)

        return buffer

    def execute(self, file_name: str, validation_flag: bool) -> None:
        print("execute")

        buffer = self.read_file(file_name)
        #print(buffer)

        if validation_flag:
            validate(instance=buffer, schema=schema)

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    #solution.execute("json_reader.json")
    solution.execute("ff9760f4-5f52-41c0-891d-257b4dff01bb", True)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
