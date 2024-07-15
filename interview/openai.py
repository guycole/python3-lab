#
# Title: openai.py
# Description: 
# 
# Code a data structure to create update delete for a map type data structure for a question 
# around maintaining a list of tuples. Sorting and merging required in follow up questions.
#
# tuple example (key, value) where key is a string and value is a string
#
import hashlib 

MAP_SIZE = 1000

class GuyItem:
    key = None
    value = None

    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"({self.key}, {self.value})"
    
    def __repr__(self) -> str:
        return f"({self.key}, {self.value})"
    
    def map_key(self) -> int:
        md = hashlib.md5()
        md.update(self.key.encode())
        temp1 = md.hexdigest() # c2add694bf942dc77b376592d9c862cd
        temp2 = int(temp1, 16)
        temp3 = temp2 % MAP_SIZE
        #print(f"temp3 {temp3}")
        return temp3

class GuyMap:
        data = [None] * MAP_SIZE
    
        def create(self, gi:GuyItem) -> None:          
            if self.data[gi.map_key()] is None:
                self.data[gi.map_key()] = [gi]
            else:
                self.data[gi.map_key()].append(gi)
     
        def delete(self, key: str) -> None:
            print(f"delete {key}")
            gi = GuyItem(key, "")
       
            if self.data[gi.map_key()] is None:
                print("delete: key not found")
            else:
                temp = self.data[gi.map_key()]
                for ndx in range(len(temp)):
                    if temp[ndx].key == key:
                        temp.pop(ndx)
                        break

        def select(self, key: str) -> GuyItem:
            gi = GuyItem(key, "")
            print(gi)

            if self.data[gi.map_key()] is None:
                pass
            else:
                for item in self.data[gi.map_key()]:
                    if item.key == key:
                        return item

            return None

        def update(self, gi:GuyItem) -> None:
            self.delete(gi.key)
            self.create(gi)

if __name__ == '__main__':
    print("main")

    item1 = GuyItem("key1", "value1")
    print(item1)
    print(item1.map_key())

    item2 = GuyItem("key2", "value2")
    print(item2)
    print(item2.map_key())

    gm = GuyMap()
    gm.create(item1)
    gm.create(item2)
    print(gm.select("key1"))
    print(gm.select("key2"))

    item3 = GuyItem("key2", "valueX")
    gm.update(item3)
    print(gm.select("key2"))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
