#
# Title: driver.py
# Description: 
# 
#

class Dtmf:

    def execute(self, file_name: str) -> str:
        print("execute")

        return "none"

if __name__ == '__main__':
    print("main")

    dtmf = Dtmf()
    print(dtmf.execute("dtmf-0.wav"))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
