#
# Title: deduper.py
# Description: delete duplicate files 
# 
import os
import sys

from model import Album, Artist, JsonParser, XmlParser
from reporter import Reporter

class DeDuplicator:

    def directory_walk(self, root_dir:str) -> list[str]:
        candidates = []

        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith(".zip"):
                    full_name = os.path.join(root, file)

                    temp = []
                    tokens = full_name.split("/")
                    for token in tokens[-3:]:
                        temp.append(token)

                    # filenames in the form p/pretenders/the_singles.zip
                    candidates.append('/'.join(temp))

        return candidates
    
    def dupe_test(self, incumbents:list[str], candidates:list[str]) -> list[str]:
        duplicates = []

        for candidate in candidates:
            if candidate in incumbents:
                duplicates.append(candidate)

        return duplicates
    
    def pruner(self, root_dir:str, targets:list[str]) -> None:
        os.chdir(root_dir)

        for target in targets:
            if os.path.exists(target):
                os.remove(target)
            else:
                print(f"missing file {target}")

    def execute(self, incumbents:str, candidates:str):
        dir1 = self.directory_walk(incumbents)
        dir2 = self.directory_walk(candidates)

        print(f"incumbents:{len(dir1)}")
        print(f"candidates:{len(dir2)}")

        duplicates = self.dupe_test(dir1, dir2)
        print(f"duplicates:{len(duplicates)}")

        self.pruner(candidates, duplicates)

#
# these two directories should be choral wave
# python deduper.py /Users/gsc/documents/audio-s3sync/choral/wave /Users/gsc/xx/audio-s3sync/choral/wave
#
if __name__ == '__main__':
    retcode = -1

    if len(sys.argv) == 3:
        incumbent = sys.argv[1]
        print(incumbent)
        candidate = sys.argv[2]
        print(candidate)

        deduper = DeDuplicator()
        retcode = deduper.execute(incumbent, candidate)
    else:
        print("missing incumbent candidate directories")

    sys.exit(retcode)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
