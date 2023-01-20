import heapq
from queue import PriorityQueue
from collections import Counter
jobs = [(1, 'eat'),(1, 'eat'),(1, 'eat'),(1, 'eat'),(1, 'eat'), (2, 'code'), (3, 'sleep')]
ht=Counter()
pq=PriorityQueue()
for task_id, username in jobs:
	ht[username]+=1
	pq.put((ht[username]*-1, task_id, username))

for _ in jobs:
	t=pq.get()
	print(t[1])
	ht[t[2]]-=1


