name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hrs = dict()
for line in handle:
    if not line.startswith("From ") : continue
    words = line.split()
    tme = words[5]
    hr = tme[:2]
    hrs[hr] = hrs.get(hr,0) + 1

lst = list()
for key, val in hrs.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)
for key, val in lst:
    print(key, val)
