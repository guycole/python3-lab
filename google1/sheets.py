#
# Title: sheets.py
# Description: google sheet driver
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import sys 

import yaml
from yaml.loader import SafeLoader

class SheetDemo:
    def __init__(self, configuration: dict[str, str]):
        pass
    

    def execute(self) -> None:
        print(f"fresh dir:{self.fresh_dir}")


print("start sheets")

#
# argv[1] = configuration filename
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        config_name = sys.argv[1]
    else:
        config_name = "config.yaml"

    configuration = {}
    with open(config_name, "r", encoding="utf-8") as in_file:
        try:
            configuration = yaml.load(in_file, Loader=SafeLoader)
        except yaml.YAMLError as error:
            print(error)

    sheet_demo = SheetDemo(configuration)
    sheet_demo.execute()

print("stop sheets")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
