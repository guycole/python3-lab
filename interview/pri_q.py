#
# Title:pri_q.py
# Description: priority queue
#

# heapq O(logn)
import heapq

# read as priority, name 
students = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'Cathy'),(4,'Lucy')] 
print(students)

heapq.heapify(students) 
# do not trust this, iterate and pop
print(students)
 
for ndx in range(5):
	temp = students.pop(0) # pull from left for priority 1 (right for max)
	heapq.heapify(students) 
	print(temp)

print(students)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
