name = raw_input("Nome do arquivo:")
handle = open(name,'r')
texto = handle.read()
palavras = texto.split()

contador = {}
for word in palavras:
	contador[word] = contador.get(word,0) + 1

big_count = None
big_word = None
for word,count in contador.items():
	if big_count is None or count > big_count:
		big_word = word
		big_count = count
print big_word,big_count