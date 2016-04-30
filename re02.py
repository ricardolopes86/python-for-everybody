import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.findall("^From:", line):
        print line
