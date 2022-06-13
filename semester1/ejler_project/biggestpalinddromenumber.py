# upgrade. works badly.

lst = []
for i in range(10, 999):
    for j in range(10, 999):
        number = str(i*j)
        k = len(number)
        n = 0
        while True:
            if number[n] == number[k-1]:
                n+=1
                k-=1
            lst.append(int(number))
# print(lst)

upper = (10**3)-1
lower = 1+upper//10
max_product = 0
lsiit = []
for i in range(upper, lower-1, -1):
    for j in range(i, lower-1, -1):
        product = i*j
        if product < max_product:
            break
        number = str(product)
        p = len(number)
        k = 0
        while k < len(number)//2 and p > len(number)//2:
            if number[k] == number[p-1]:
                k+=1
                p-=1
            lsiit.append(number)
# print(lsiit)