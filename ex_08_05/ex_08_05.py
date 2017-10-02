fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From ") : continue
    adr = line.split()
    print(adr[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")
