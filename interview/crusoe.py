# INITIALIZATION CODE MUST BE KEPT
# populate the directory structure
import tarfile
tar = tarfile.open("/home/coderpad/data/files.tar.gz", "r:gz")
tar.extractall()
tar.close()
# WRITE SOLUTION BELOW HERE

# This folder structure contains many files. Write code to provide me with:

# 1. A count of files that have unqiue content (no other file shares their content)
# 2. A list of all duplicate files grouped by content.
# 3. Explain how to optimize and scale your code.

import logging
import os
from typing import List
import hashlib


# return a list of:
#  * list of all files with the same content
# log the number of files that have no duplicates
def find_duplicates(path: str) -> List[List[str]]:
    dd = {}
    
    for current_dir, directories, files in os.walk(path):
        # logging.warn(f"{current_dir} contains {files}")

        for file in files:
            fullpath = f"{current_dir}/{file}"
            #print(fullpath)

            try:
                with open(fullpath, 'rb') as infile:
                    buffer = infile.read()

                    h = hashlib.new('md5')
                    h.update(buffer)
                    results = h.hexdigest()
                    # print(results)
                    
                    if results in dd:
                        dd[results].append(fullpath)
                    else:
                        dd[results] = [fullpath]

            except Exception as error:
                print(error)

    no_dupe_counter = 0
    ret_list = []
    for key, value in dd.items():
        if len(value) > 1:
            print(f"duplicates {value}")
            ret_list.append(value)
        else:
            no_dupe_counter += 1

    print(f"no duplicate count {no_dupe_counter}")

    return ret_list

dups = find_duplicates(".")
for x in dups:
    f = x[0]
    with open(f, "rb") as fh:
        print(fh.read())
