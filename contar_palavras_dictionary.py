counts = dict()
names = ["ricardo","ludmila","carla","raissa","sara","azle","ricardo","carlos","carla","ludmila"]
for nome in names:
	if nome not in counts:
		counts[nome] = 1
	else:
		counts[nome] = counts[nome] + 1
# um loop para fazer o mesmo que acima, porém muit mais rapido e simples:
#	for name in names:
#		counts[name] = counts.get(nome,0) + 1

print counts