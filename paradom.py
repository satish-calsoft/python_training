##########paradom##########
a = []
for j in range(500):
	b = [int(i) for i in str(j)]
	if b[0] == b[-1]:
		a.append(b)
print a
