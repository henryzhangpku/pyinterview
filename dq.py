from collections import deque
jobs = [(1, 'eat'),(1, 'eat'),(1, 'eat'),(1, 'eat'),(1, 'eat'), (2, 'code'), (3, 'sleep')]
q=deque()
for task_id, username in jobs:
	q.append(task_id)

for _ in jobs:
	t=q.popleft()
	print(t)


