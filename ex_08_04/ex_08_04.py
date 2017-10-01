lst = list()

fname = input("Enter file name: ")
fh = open(fname)

fh = fh.read()
fh = fh.split()
for word in fh:
    if word not in lst:
        lst.append(word)

print(lst)
