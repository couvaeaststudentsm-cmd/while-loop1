students = {"Tom":90,"Maya":89,"leo":79,"Zoe":86,"sam":84,"shiva":98}
print("Students Grades:")

for name,grade in students.items():
    print(name,":",grade)

average = sum(students.values()) / len(students)
print("\nClass Average:",average)

top_student = max(students,key=students.get)
print("Top scorer:",top_student,"-",students[top_student])

bottom_student = min(students,key=students.get)
print("bottom scorer:",bottom_student,"-",students[bottom_student])

search = 'shiva'

if search in students:
    print("\nGrade of ",search,":",students[search])
else:
    print("\nStudent not found.")