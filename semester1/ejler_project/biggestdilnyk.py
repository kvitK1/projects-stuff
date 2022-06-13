# upgrade. works badly

num = 600851475143
num1 = 13195
dilnyks_array = []

def checker(num):
    counter = 0
    for i in range(2, num+1):
        if num%i==0:
            counter += 1
    if counter > 1:
        return False
    else:
        return True

for dil in range(2, num1+1):
    if num1%dil == 0:
        if checker(dil) == True:
            dilnyks_array.append(dil)

print(max(dilnyks_array))





