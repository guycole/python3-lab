#
# Title: verifier.py
# Description: 
# 
from model import Album, Artist, Parser

class Verifier:

    def execute(self, file_name: str) -> None:
        print("execute")

        parser = Parser()
        album = parser.reader(file_name)
        print(album)

        return

if __name__ == '__main__':
    verifier = Verifier()
    result = verifier.execute("choral_wave/manifest.xml")
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
