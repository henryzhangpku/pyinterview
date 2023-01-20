from collections import Counter
import heapq
jobs = [(1, 'eat'),(1, 'eat'),(1, 'eat'),(1, 'eat'),(1, 'eat'), (2, 'code'), (3, 'sleep')]
ht=Counter()
a=[]
heapq.heapify(a)
for task_id, username in jobs:
	ht[username]+=1
	heapq.heappush(a, (ht[username], task_id, username))

for _ in jobs:
	t=heapq.heappop(a)
	print(t[1])
	ht[t[2]]-=1


