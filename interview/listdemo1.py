
list1 = [2, 7, 11, 15]

ranger = [ii for ii in range(len(list1))]

for ndx1 in ranger:
    for ndx2 in ranger[1+ndx1:]:
#        print(f"test {ndx1} {ndx2}")
        if list1[ndx1] + list1[ndx2] == 9:
            print(f"hit {ndx1} {ndx2}")

print("------")

list1 = [3, 2, 4]

ranger = [ii for ii in range(len(list1))]

for ndx1 in ranger:
    for ndx2 in ranger[1+ndx1:]:
#        print(f"test {ndx1} {ndx2}")
        if list1[ndx1] + list1[ndx2] == 6:
            print(f"hit {ndx1} {ndx2}")

print("------")

list1 = [-2, 11, -4, 13, -5, -2]

ranger = [ii for ii in range(len(list1))]

maxx = -9999
for ndx1 in ranger:
    for ndx2 in ranger[1+ndx1:]:
#        print(f"test {ndx1} {ndx2}")
#        print(list1[ndx1:ndx2+1])
        temp = sum(list1[ndx1:ndx2+1])
        if temp > maxx:
            maxx = temp
            print(f"fresh max {maxx}")

##########

list1 = [1, 8]
list2 = [0]

#list1 = [2, 4, 3]
#list2 = [5, 6, 4]
result = []

len_list1 = len(list1)
len_list2 = len(list2)

if len_list1 > len_list2:
    ranger = [ii for ii in range(len(list1))]
else:
    ranger = [ii for ii in range(len(list2))]

carry = 0
result = []
for ndx1 in ranger:
    addend1 = 0
    addend2 = 0

    try:
        addend1 = list1[ndx1]
    except:
        pass

    try:
        addend2 = list2[ndx1]
    except:
        pass

    sum1 = addend1 + addend2 + carry

    if sum1 > 9:
        sum1 = sum1 - 10
        carry = 1
    else:
        carry = 0

    result.append(sum1)

print(result)