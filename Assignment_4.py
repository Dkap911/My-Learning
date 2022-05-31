#Assignment 4.1
def computepay(h, r):
    if h>40:
        pay=(40*r)+(r*1.5*(h-40))
    else:
    	pay=h*r
    return pay
hrs = input("Enter Hours:")
rate= input("Enter Rates:")

p = computepay(float(hrs), float(rate))

print("Pay", p)
