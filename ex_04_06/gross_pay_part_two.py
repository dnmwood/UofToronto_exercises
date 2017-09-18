def computepay(h,r):
    hrs = float(h)
    rte = float(r)
    if hrs <= 40:
        return(hrs * rte)
    elif hrs > 40:
        oth = (hrs - 40)
        otr = (rte * 1.5)
        return(40 * rte + (oth * otr))

h = input("Enter Hours:")
r = input("Enter Rate:")
pay = computepay(h,r)
print(pay)
