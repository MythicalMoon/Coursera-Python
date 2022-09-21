t = ['a', 'b', 'c', 'd', 'e', 'f']
t.reverse()
print(t)
f = sorted(t) # keeps original intact where t.sort modifies
print(f)
print(t)