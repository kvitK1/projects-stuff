from math import cos, pi
import matplotlib.pyplot as plt


def work_with_input():
    '''Defines the input for the following work with the programm.'''
    print('Here`s the function we`ll set to taylor series in a moment..')
    print("y = (cos(3*x))**3")
    print('do you want the x to be in radians (R) or degrees (D)?')
    while True:
        value_type = input('>>> Enter R or D: ')
        if value_type.lower() == 'r' or value_type.lower() == 'd':
            break
    while True:
        value = input('>>> Enter the value of x: ')
        try:
            if value_type.lower() == 'd':
                value = deg_to_rad(float(value))
                break
            elif value_type.lower() == 'r':
                value = float(value)
                break
        except ValueError:
            print('You entered something wrong! try again')
    while True:
        terms = input('>>> Enter a positive integer number, \
that will be the number of terms in Taylor series: ')
        try:
            if int(terms) <= 0:
                print('OOps, try again!')
            else:
                terms = int(terms)
                break
        except ValueError:
            print('You entered something wrong, try again!')
    return value, terms


def factorial(num):
    '''Function to count factorial.'''
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)


def formula(arg, n):
    '''Function that repsresents the formula.'''
    result1 = 0
    result2 = 0
    for i in range(n+1):
        result1 += (((-1)**i)*((3*arg)**(2*i)))/factorial(2*i)
        result2 += (((-1)**i)*((9*arg)**(2*i)))/factorial(2*i)
    result = (3*result1 + result2)/4
    return result

def mistake_range(arg, mist):
    '''Function that counts how many terms you need to reach the value,
    not bigger than 10**(-n)'''
    try:
        counter = 0
        stand_cos = (cos(3*arg))**3
        while True:
            if abs(formula(arg, counter)-stand_cos) > mist:
                counter += 1
            else:
                return counter
    except:
        return 'I can`t reach the number of terms, sorry'


def deg_to_rad(ang):
    '''Transform degrees to radians.'''
    return (ang*pi)/180


def draw_graphs(value, terms=50):
    '''Draws a graph of fucntion approximation.'''
    x_coord = list(range(terms+1))
    my_func = []
    built_func = (cos(3*value))**3
    for i in x_coord:
        my_func.append(formula(value, i))

    plt.plot(x_coord, my_func, color='red')
    plt.plot(x_coord, [built_func]*len(x_coord), color='green')
    plt.show()


if __name__ == '__main__':
    try:
        x, n = work_with_input()
        print(f'Here`s the result: {formula(x, n)}')
        print(f'And that`s what the built-in function shows: {(cos(3*x))**3}')
        print(f'Number of terms, so the difference <= 0.1: {mistake_range(x, 10**(-1))}')
        print(f'Number of terms, so the difference <= 0.001: {mistake_range(x, 10**(-3))}')
        print(f'Number of terms, so the difference <= 0.000001: {mistake_range(x, 10**(-6))}')
        draw_graphs(x)
        print('Thank you for your interest! Come again!')
    except OverflowError:
        quit("Oops, it seems you`ve entered too large number")
