r = 0
n = input()
for i in range(n):
    p = 0
    s = 0
    a,b,c = raw_input().split()
    r = int(a) * int(b) + int(c)
    while(r!=0):
        p = r%10
        r = r/10
        s = s+p
    print s,