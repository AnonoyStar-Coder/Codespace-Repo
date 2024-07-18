x = {1,3,8.6,7.5,3}
print(x)
print()

y = {1,3,8.6,7.5,3,"python"}
print(y)
print()

# x.add("C++")
# print(x)
# print()
# x.discard("C++")

# x.discard("8")
# print(x)
# print()
# x.add("8")

c = y.difference(x)
print(c)
print()

d = x.union(y)
print(d)
print()

e = x.intersection(y)
print(e)
print()

f = x.issubset(y)
print(f)
print()

g = x.issuperset(y)
print(g)