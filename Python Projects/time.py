import math

n = input()

for i in range(n):
    a,b,c,d = raw_input("1st").split()
    e,f,g,h = raw_input("2nd").split()

    seconds = int(f+g+h) - int(b+c+d)
    print seconds

    days = int(e) - int(a)
    print "Days :",days

    SecondsInHour = 3600
    hours = seconds / SecondsInHour
    print "Hour :",hours

