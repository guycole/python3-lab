# Implement a dictionary that supports point-in-time lookups.

# Expected API:

#   get(key, timestamp=None)
#   put(key, value)

# The semantics should be chosen so that, if a timestamp is provided,
# the dictionary behaves exactly like it would have at that point in time.

# Don't worry about performance, but do write this as if it were
# production code you'd be happy to check in.

# Example:

# put('AI', 'A')                # timestamp = 10
# put('AI', 'B')                # timestamp = 12
# put('AI', 'C')                # timestamp = 14

# # timestamp = 15
# get('AI')                   # Returns 'C'
# get('AI', timestamp=13)     # Returns 'B'
# get('AI', timestamp=10)     # Returns 'A'
# get('AI', timestamp=5)      # Exception; key does not exist at t=5

class FancyMap:
  def __init__(self):
    self.fm = {}
    self.time_stamp = 0

  def get_time_stamp(self):
    self.time_stamp += 2
    return self.time_stamp

  def get(self, key, time_stamp=None):
    if key not in self.fm:
      return None

    candidates = self.fm[key]
    selected = None

    if time_stamp is None:
      # latest time stamp is at the end of list
      selected = candidates[-1]
    else:
      # list sorted by time, oldest is first
      for ndx in range(len(candidates)-1, -1, -1):
        #print(f"{candidates[ndx][0]} {time_stamp}")
        if candidates[ndx][0] <= time_stamp:
          #print(f"{ndx} {candidates[ndx]}")
          selected = candidates[ndx]
          break

    return selected 

  def put(self, key, value) -> tuple:
    container = (self.get_time_stamp(), value)

    if key in self.fm:
      # key collision
      self.fm[key].append(container)
    else:
      # fresh key
      self.fm[key] = [container]

    return container

fm = FancyMap()
fm.put('AI', 'A')
fm.put('AI', 'B')
fm.put('AI', 'C')

print(fm.fm)
print(fm.get('AI'))
print(fm.get('AI', time_stamp=6))
print(fm.get('AI', time_stamp=7))
print(fm.get('AI', time_stamp=5))
print(fm.get('AI', time_stamp=3))
