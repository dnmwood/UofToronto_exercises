hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter rate:")
r = float(rte)

#overtime
othrs = (h - 40)
otrte = (r * 1.5)

#regular hours
if h <= 40:
	print(h * r)
#overtime hours
elif h > 40:
    print((40 * r) + (othrs * otrte))
