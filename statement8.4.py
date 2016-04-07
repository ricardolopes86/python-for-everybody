fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
final_lst = list()
arquivo = fh.read()
lst = arquivo.split()
for line in lst:
	if line not in final_lst:
		final_lst.append(line)
final_lst.sort()
print final_lst