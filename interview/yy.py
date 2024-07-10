dummy = ['a'] * 5
print(dummy)
cloned = dummy.copy()

targets = ['a', 'b', 'c']

for ndx1 in range(len(targets)):
  for ndx2 in range(ndx1+1, len(targets)):
    print(f"{targets[ndx1]} {targets[ndx2]}")

lc = [x for x in range(11) if x % 2 == 0]
print(lc)

try:
  with open('bogus', 'r') as infile:
    infile.readlines()
except Exception as error:
  print(error)

print(''.join(targets))
print(''.join(targets[::-1]))

dd = {'a':1, 'b':2, 'c':3, 'd':2}
selected = [key for key, value in dd.items() if value == 2]
print(selected)

for key in dd.keys():
  print(f"{key} {dd[key]}")

results = sorted(dd.items(), key=lambda x:x[1], reverse=True)
print(results)
