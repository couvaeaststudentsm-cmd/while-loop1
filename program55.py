set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

print("Set 1 :",set1)
print("Set 2 :",set2)

print("\nUnion of two sets:")
print(set1.union(set2))

print("\nIntersection of two sets:")
print(set1.intersection(set2))

print("\nDifference(Set2 - Set1):")
print(set1.difference(set2))

print("\nDifference(Set1 - Set2):")
print(set2.difference(set1))

print("\nSymmetric Difference:")
print(set1.symmetric_difference(set2))

set1.add(80)
print("\nAfter adding 80:")
print(set1)

set1.remove(20)
print("\nAfter removing 20:")
print(set1)

set2.clear()
print("\nAfter clearing Set2:")
print(set2)