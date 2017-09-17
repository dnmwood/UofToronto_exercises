def computepay(hrs,rte):
    hrs = float(hrs)
    rte = float(rte)
    if hrs <= 40:
        return(hrs * rte)
    elif hrs > 40:
        oth = hrs - 40
        otr = (rte * 1.5)
        return(40 * rte + (oth * otr))



hrs = input("Enter Hours:")
rte = input("Enter Rate:")
p = computepay(hrs,rte)
print(p)
