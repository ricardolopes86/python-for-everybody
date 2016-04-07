def computepay(h,r):
    if h <= 40:
        pay = h * r
        return pay
    else:
        pay = r * 40 + (r * 1.5 * (h - 40))
        return pay
inp = raw_input("Enter Hours:")
hora = float(inp)
inp = raw_input("Enter rate:")
rate = float(inp)
p = computepay(hora,rate)
print "Pay",p