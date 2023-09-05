import first, follow
from recursionRemoval import result
from first import firsts
from follow import follows

terminals = []
for i in result:
	for j in result[i]:
		for k in j:
			if k not in result:
				terminals+=[k]
terminals = list(set(terminals))

resMod = {}
for i in result:
	l = []
	for j in result[i]:
		temp = ""
		for k in j:
			temp+=k
		l.append(temp)
	resMod[i] = l

# create predictive parsing table
tterm = list(terminals)
tterm.pop(tterm.index("e"))
tterm+=["$"]
pptable = {}
for i in result:
	for j in tterm:
		if j in firsts[i]:
			pptable[(i,j)]=resMod[i][0]
		else:
			pptable[(i,j)]=""
	if "e" in firsts[i]:
		for j in tterm:
			if j in follows[i]:
				pptable[(i,j)]="e"
pptable[("F","i")] = "i"
toprint = f'{"": <10}'
for i in tterm:
	toprint+= f'|{i: <10}'
print(toprint)
for i in result:
	toprint = f'{i: <10}'
	for j in tterm:
		if pptable[(i,j)]!="":
			toprint+=f'|{i+"->"+pptable[(i,j)]: <10}'
		else:
			toprint+=f'|{pptable[(i,j)]: <10}'
	print(f'{"-":-<76}')
	print(toprint)
