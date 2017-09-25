# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('file not found:', fname)
    quit()

fh = fh.read()
fh = fh.rstrip()
fh = fh.upper()
print(fh)
