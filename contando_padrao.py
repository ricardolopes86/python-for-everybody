counts = dict()
print "Enter a line of text"
line = raw_input()

words = line.split()
print "Words:",words

print "Contando"
for word in words:
	counts[word] = counts.get(word,0) + 1

print "Valor:",counts