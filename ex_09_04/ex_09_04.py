emails = dict()
most_emails = -1

name = input("Enter file: ")
if len(name) < 1 : name = "mbox.txt"
handle = open(name)

for line in handle:
    if not line.startswith("From ") : continue
    words = line.split()
    e = words[1]
    emails[e] = emails.get(e,0) + 1
    if emails[e] > most_emails:
        most_emails += 1

for e in emails:
    if emails[e] == most_emails:
        print(e, emails[e])
