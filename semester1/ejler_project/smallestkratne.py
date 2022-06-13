numbers = [*range(1, 10)]
numeryk = 0
for n in numbers:
    numeryk += n
print(numeryk)

def bip(numlist):
    lst = []
    for num in range(numlist, numlist**2):
        for number in numbers:
            if num%number:
                lst.append((num, number))
                return True
    print(lst)
            
bip(numeryk)