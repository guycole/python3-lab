import json

def dictionary_compare(d1, d2):
    for k1 in sorted(d1.keys()):
        if k1 in d2.keys():
            if d1[k1] != d2[k1]:
                print(f"different value {d1[k1]}")

            if str(type(d1[k1])) == "<class 'str'>":
                print('string noted')
            elif str(type(d1[k1])) == "<class 'list'>":
                print("list noted")
            elif str(type(d1[k1])) == "<class 'dict'>":
                print("dict noted")

            print(type(d1[k1]))
            print(str(type(d1[k1])))
        else:
            print(f"d2 is missing {k1}")

    for k2 in sorted(d2.keys()):
        if k2 in d1.keys():
            if d1[k2] != d2[k2]:
                print(f"different value {d2[k2]}")
        else:
            print(f"d1 is missing {k2}")

def diff1(d1, d2, path=""):
    for k in d1.keys():
        if not k in d2.keys():
            print(path, ":")
            print(k + " as key not in d2", "\n")
        else:
            if type(d1[k]) is dict:
                if path == "":
                    path = k
                else:
                    path = path + "->" + k
                diff1(d1[k],d2[k], path)
            else:
                if d1[k] != d2[k]:
                    print(path, ":")
                    print(" - ", k," : ", d1[k])

if __name__ == '__main__':
    print("main")

    d1 = json.loads('''{}''')
    print(d1)

    d2a = json.loads('''{"key1":"value", "key0":"value"}''')
    d2b = json.loads('''{"key2":"value", "key0":"value"}''')
    print(d2a)
    dictionary_compare(d2a, d2b)

    d3a = json.loads('''{"key":["value1", "value2"]}''')
    d3b = json.loads('''{"key":["value1", "value2"]}''')
    dictionary_compare(d3a, d3b)

    d4a = json.loads('''{"a":{"a":"b"}}''')
    d4b = json.loads('''{"a":{"a":"b"}}''')
    dictionary_compare(d4a, d4b)

    d5a = json.loads('''{"a":["b", "c", {"x":"y"}]}''')
    print(d5a)

    xx = json.dumps(d5a)
    print(xx)

#    d3 = json.loads('''{"key":["value1", "value2"]}''')
#    print(d3)

#    d4 = json.loads('''{"key1":{"key2":{"key3":"value1"}}}''')
#    print(d4)

#    d5 = dict((k, v) for k, v in d4.items())
#    print(d5)

#    d6 = json.loads('''{"a":{"a":"b"}}''')
#    print(type(d6))
#    print(d6)