name = raw_input("Nome do arquivo:")
handle = open(name,'r')

contador = dict()
for line in handle:
	if line.startswith("From "):
		palavras = line.split()
		for palavra in palavras:
			if '@' in palavra:
				contador[palavra] = contador.get(palavra,0) + 1

big_count = None
big_word = None
for word,count in contador.items():
	if big_count is None or count > big_count:
		big_word = word
		big_count = count
print big_word,big_count