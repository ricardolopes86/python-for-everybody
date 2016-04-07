# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
value = 0
avg = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    position = line.find(" ")
    value = line[position+1:]
    count = count + 1
    avg = avg + float(value)
avg_final = avg / count
print "Average spam confidence:",avg_final