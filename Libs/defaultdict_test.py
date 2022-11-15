grades = [
	('elliot', 91),
	('neelam', 98),
	('bianca', 81),
	('elliot', 88),
]
print(grades)
from collections import defaultdict
student_grades = defaultdict(list) #dict<list>
for name, grade in grades:
	student_grades[name].append(grade)

print(student_grades)