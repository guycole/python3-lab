def diff1(dl, dr, p=''):
    for key_left in sorted(dl):
        if key_left in dr:
            print(f"both {key_left}")
            print(type(dl[key_left]))
            if type(dl[key_left]) is int:
                print("int noted")
                if dl[key_left] == dr[key_left]:
                    print("match")
                else:
                    print(f"-$.{p}.{key_left} {dl[key_left]}")
                    print(f"+$.{p}.{key_left} {dr[key_left]}")
            elif type(dl[key_left]) is dict:
                print("dict noted")
                if type(dr[key_left]) is dict:
                    diff1(dl[key_left], dr[key_left], key_left)
        else:
            print(f"-$.{p}.{key_left} {dl[key_left]}")

if __name__ == '__main__':
    print('main')

#    dl = { "a":1, "b":"3"}
#    dr = { "a":2 }

#    diff1(dl, dr)

    dl ={"a":{"b":1}}
    dr ={"a":{"b":2}}

    diff1(dl, dr)


