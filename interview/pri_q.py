#
# Title:pri_q.py
# Description: priority queue
#
# https://realpython.com/python-heapq-module/
#
# heapq is a minheap O(log n)
# can make maxheap by multplying all candidates by -1
#
import heapq

# read as priority, name 
students = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'Cathy'),(4,'Lucy')] 
print(students)

heapq.heapify(students) # O(n) minheap
print(students)

print(heapq.heappop(students))
print(heapq.heappop(students))
print(heapq.heappop(students))
print(heapq.heappop(students))
print(heapq.heappop(students))

print(students)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
