# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('file not found:', fname)
    quit()

count = 0
xtotal = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find('0')
    xval = line[pos:pos+6]
    for x in xval:
        x = float(xval)
        count = count + 1
        xtotal = xtotal + x

print('Average spam confidence:', xtotal / count)
