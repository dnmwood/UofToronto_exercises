import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_29785.txt"
handle = open(name)
x = handle.read()

# List of numbers
numlist = re.findall('[0-9]+', x)

# Convert to integers and add to total_num
total_num = 0
for x in numlist:
    x = int(x)
    total_num += x

print(total_num)
