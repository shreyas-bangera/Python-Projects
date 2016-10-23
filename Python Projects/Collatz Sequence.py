d = input()
value = 0
avg = 0

for i in range(d):
    data = raw_input()
    for j in range(len(data)):
        s = sum(data)

div = len(data) -1
avg = s / div
print s
print avg
