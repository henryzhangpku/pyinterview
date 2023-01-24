from queue import PriorityQueue
from collections import Counter
class TaskScheduler():
	def __init__(self):
		self.pq=PriorityQueue()
		self.c=Counter()
	def submit_task(self, task_id, username):
		self.c[username]+=1
		self.pq.put((self.c[username], task_id, username))

	def next_task_no(self):
		if self.pq.empty():
			return -1
		t=self.pq.get()
		self.c[t[2]]-=1
		return t

ts=TaskScheduler()
jobs = [(1, 'tom'),(1, 'tom'),(1, 'tom'),(1, 'tom'),(1, 'tom'), (2, 'jack'),(2, 'jack'), (3, 'marry'), (3, 'marry')]
for j in jobs:
	ts.submit_task(j[0],j[1])
for _ in jobs:
	print(ts.next_task_no())



