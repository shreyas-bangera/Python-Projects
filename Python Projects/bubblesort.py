#n = raw_input()

str_arr = raw_input().split(' ')
array = [int(num) for num in str_arr]

for i in range(len(array)-1):
    if array[i] >= array[i+1]:
       t = array[i]
       array[i] = array[i+1]
       array[i+1] = t

print array[i],
    #3 1 4 1 5 9 2 6