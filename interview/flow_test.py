# A resident living in a Flow building can earn points by attending events. The available events are represented as a 2D array, with each entry being [eventId, startsAt, endsAt, points]. 
# e.g.
# [
#     [1, 8, 9, 100], // Morning Yoga
#     [2, 8, 9, 50], // Rooftop lunch
#     [5, 17, 18, 20] // Evening social
# ]
# Return the max number of points the resident can earn, with the list of related eventIds.

class Container:
    id = None
    start_time = None
    end_time = None
    points = 0

    def __init__(self, args):
        self.id = args[0]
        self.start_time = args[1]
        self.end_time = args[2]
        self.points = args[3]

    def __repr__(self):
        return f"Container: {self.id}, {self.start_time}, {self.end_time}, {self.points}"

    def __str__(self):
        return f"Container: {self.id}, {self.start_time}, {self.end_time}, {self.points}"

    def __copy__(self):
        new_instance = Container(self.id, self.start_time, self.end_time, self.points)
        return new_instance
        
def max_points(candidates) -> list[Container]:
    buffer = []
    results = []
    temp = []
    
    # print(candidates)
    
    for ndx1 in candidates:
        buffer.append(Container(ndx1))

    # print(buffer)

    # discover the max points for each hour
    for hours in range(24):
        temp.clear()
        for ndx1 in buffer:
            if ndx1.start_time == hours:
                temp.append(ndx1)

        #print(temp)
        # temp now contains all the events that start at this hour
        # discover the max item
        max_ndx = -1
        max_points = -1
        for ndx2 in range(len(temp)):
            if temp[ndx2].points > max_points:
                max_points = temp[ndx2].points
                max_ndx = ndx2

        if max_ndx > -1:
            results.append(temp[max_ndx])
        
    return results
    
if __name__ == '__main__':
    test_val = [
        [1, 8, 9, 100], # Morning Yoga
        [2, 8, 9, 50], # Rooftop lunch
        [5, 17, 18, 20] # Evening social
    ]
    
    # id collission
    # start collission
    # end time before start time
    # points are always positive
    # should verify correct max value
    # is duration only one hour?  

    results = max_points(test_val)
    print(results)