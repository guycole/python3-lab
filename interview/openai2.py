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

class Solution:
    fake_time = 8

    def get_timestamp(self) -> int:
        self.fake_time = self.fake_time + 2
        return self.fake_time

    actual = {}
    wrapper = {}

    def put2(self, key, value) -> None:
        current_time = self.get_timestamp()
        tweaked = (current_time, key, value)
#        print(tweaked)

        if key in self.actual:
            temp = self.actual[key]
            temp.append(tweaked)
            self.actual[key] = temp
        else:
            self.actual[key] = [tweaked]

    def get2(self, key, timestamp=None):
        if key in self.actual:
            temp = self.actual[key]
            if timestamp is None:
                winner = temp[len(temp)-1]
                return winner
            else:
#                print(f"seeking {timestamp}")
#                print(temp)
                for ndx2 in range(len(temp)-1, -1, -1):
#                    print(ndx2)
                    candidate = temp[ndx2]
#                    print(candidate)
                    ts = candidate[0]
#                    print(f"have {ts}")
                    if ts <= timestamp:
#                        print(f"returning {ts}")
                        return temp[ndx2]

                raise Exception("not found")
        else:
            return None

solution = Solution()
solution.put2('AI', 'A')           
solution.put2('AI', 'B')              
solution.put2('AI', 'C')  

print(solution.actual)

print(solution.get2('AI'))
print(f"returned {solution.get2('AI', timestamp=13)}")
print(solution.get2('AI', timestamp=10))
print(solution.get2('AI', timestamp=5))

# get('AI')                   # Returns 'C'
# get('AI', timestamp=13)     # Returns 'B'
# get('AI', timestamp=10)     # Returns 'A'
# get('AI', timestamp=5)      # Exception; key does not exist at t=5
#print(actual)

