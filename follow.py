import first
import recursionRemoval
from recursionRemoval import result
from first import firsts

def follow(gram, term):
	a = []
	for rule in gram:
		for i in gram[rule]:
			if term in i:
				temp = i
				indx = i.index(term)
				if indx+1!=len(i):
					if i[-1] in firsts:
						a+=firsts[i[-1]]
					else:
						a+=[i[-1]]
				else:
					a+=["e"]
				if rule != term and "e" in a:
					a+= follow(gram,rule)
	return a

follows = {}
for i in result:
	print(f'First({i}):', firsts[i])
	follows[i] = list(set(follow(result,i)))
	if "e" in follows[i]:
		follows[i].pop(follows[i].index("e"))
	follows[i]+=["$"]
	print(f'Follow({i}):',follows[i])