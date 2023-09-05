import recursionRemoval
from recursionRemoval import result

def first(gram, term):
	a = []
	if term not in gram:
		return [term]
	for i in gram[term]:
		if i[0] not in gram:
			a.append(i[0])
		elif i[0] in gram:
			a += first(gram, i[0])
	return a

firsts = {}
for i in result:
	firsts[i] = first(result,i)
	# print(f'First({i}):',firsts[i])


# 	temp = follow(result,i,i)
# 	temp = list(set(temp))
# 	temp = [x if x != "e" else "$" for x in temp]
# 	print(f'Follow({i}):',temp)




