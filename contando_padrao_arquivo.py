counts = dict()
print "Enter the name of text file:"
arquivo = raw_input()
fh = open(arquivo)

print "Contando"
for line in fh:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

print "Valor:",counts
print "Valor para o From:",counts["From"]