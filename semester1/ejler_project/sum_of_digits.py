# number1 = [int(i) for i in str(2**15)]
number2 = [int(i) for i in str(2**1000)]
res2 = 0
for dig in number2:
    res2 += dig
print(res2)

# 2 var
num = sum(map(int, str(2**1000)))
print(num)
