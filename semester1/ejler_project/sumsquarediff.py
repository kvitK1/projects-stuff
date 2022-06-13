n = 100
counter1 = 0
counter2 = 0 
for i in range(1, n+1):
    counter1 += i**2
    counter2 += i
print(counter2**2-counter1)