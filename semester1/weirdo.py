num = int(input())
count = 0

# -- search for simple numbers --
def check_for_simpl_num(num):
    counter = 2
    while counter < num:
        if num%counter == 0:
            break
        else:
            counter += 1
            if counter == num:
                print(counter)

while count != num:
    check_for_simpl_num(count)
    count += 1



# -- prints the sum of all inputs
#  while input != 0 --
num = int(input())
count = 0
while num != 0:
    count += num
    num = int(input())
print(count)



#  -- the best choice, prints the sum of all inputs
#  while input != 0 --
while True:
    num = int(input())
    if num != 0:
        count += num
    else:
        break
print(count)



# -- a game "guess the number" --

import random

num = random.randint(0, 100)

while True:
    number = int(input())
    if number > num:
        print('ти ввів більше число')
    elif number < num:
        print('ти ввів менше число')
    else:
        print('ти відгадав!')
        break



# -- 'for' loop, checking if input is in list --
item_list = ['apple', 'banana', 'orange']
user_item = input()
isproduct = False
for item in item_list:
    if user_item == item:
        isproduct = True
        print(f'{user_item} is in your list!')
        break
if not isproduct:
    print('don`t buy this')



# -- building a square with '*' --
num = 10
for rows in range(num):
    for columns in range(num):
        print('*', end="")
    print()
    