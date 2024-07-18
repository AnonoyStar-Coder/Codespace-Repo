#tuple

tuple1=(3,5,9,84,2,4,2,5,5,8,4,6,.65,6.593)
print(tuple1)

#making tuple mutable: changing from tuple to list

print("assigning")
x = list(tuple1)
print()

print("x = list(tuple1)")
print()

print("making changes")
x.append("hello")
print("use append command")
print()

print("overridding")
tuple1 = tuple(x)
print("tuple1 = tuple(x)")
print()

print("confirming changes")
print(tuple1)