from queue import PriorityQueue
from collections import Counter
jobs = [(1, 'tom'),(1, 'tom'),(1, 'tom'),(1, 'tom'),(1, 'tom'), (2, 'jack'),(2, 'jack'), (3, 'marry'), (3, 'marry')]
ht=Counter()
pq=PriorityQueue()
for task_id, username in jobs:
	ht[username]+=1
	pq.put((ht[username], task_id, username))

for _ in jobs:
	t=pq.get()
	print(t[1])
	ht[t[2]]-=1


