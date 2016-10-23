n = input("Enter max value")
median = 0
for i in range(n):
    a,b,c = raw_input("Enter values for a b and c").split()
    if((b > a or c > a) and (b < a or c < a)):
        median = a
    elif((a > b or c > b) and (a < b or a < c)):
        median = b
    elif((a > c or b > c) and (a < c or b < c)):
        median = c
    print median,

