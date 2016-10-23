num = raw_input()
#array = []


str_arr = raw_input().split(' ')
array = [int(num) for num in str_arr]
x = len(array) - 1

for i in range(len(array)):
    value = array[x]
    print value,
    x -= 1
