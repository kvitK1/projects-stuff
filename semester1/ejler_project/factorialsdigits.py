def factorial(number):
    if number == 1:
        return 1
    elif number == 0:
        return 1
    else:
        return number*factorial(number-1)


def factor_digits(num1, num2):
    for number in range(num1, num2+1):
        sum = 0
        number_list = [int(i) for i in list(str(number))]
        for digit in number_list:
            sum += factorial(digit)
        if sum == number:
            print(f"sum {sum} == {number}")

factor_digits(10, 1987345)

