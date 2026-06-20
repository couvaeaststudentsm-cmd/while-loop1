student = {'name': 'Rahul','age':15,"marks":85,"city":"Delhi"}

print("Orginal Dictionary:")
print(student)

print("\nAcessing values:")
print("Name:",student["name"])
print("Marks:",student.get("marks"))

student['grade'] = 10
print("\nAfter Adding Grade:")
print(student)

student['marks'] = 95
print("\nAfter Adding Marks:")
print(student)

student.pop('age')
print("\nAfter pop operation:")
print(student)

student.popitem()
print("\nAfter popitem operation:")
print(student)

if 'name' in student:
    print("\nName key exists")
else:
    print("\nName key doesn not exist")

print("\nkeys of dictionary:")
print(student.keys())

print('\nValues of Dictionary:')
print(student.values())

print('\nItems of Dictionary:')
print(student.items())

new_student = student.copy()
print("\nCopied Dictionary:")
print(student)

student.clear()
print("\nAfter Clear Operation")
print(student)