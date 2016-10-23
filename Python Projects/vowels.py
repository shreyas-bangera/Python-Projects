n = input("Enter max value")

for i in range(n):
    vowels = 0
    input = raw_input("Enter a sentence")
    for l in input:
        if(l in  ['a','e','i','o','u','y']):
            vowels = vowels + 1
    print vowels,
