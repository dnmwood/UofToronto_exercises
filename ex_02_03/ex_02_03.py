hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter rate:")
r = float(rte)

oth = h - 40
if h <= 40:
	print(h * r)
elif h > 40:
    print((40 * r) + (oth * (r * 1.5)))
