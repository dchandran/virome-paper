import sys

l = []

for line in open(sys.argv[1]):
    line = line.rstrip()
    l.append(line)

for x in l:
    print "rownames(ann) == ",
    print '''"''' + x + '''" | ''', 
