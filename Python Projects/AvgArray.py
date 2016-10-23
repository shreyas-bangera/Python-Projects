n = input()
val = 0
for i in range(n):
    data = raw_input().split(' ')
    l = len(data) -1
    for d in data:
        val = val + int(d)
        result = val / l
        print result,