# https://www.hackerrank.com/challenges/py-if-else/problem

n = 3

if n % 2 != 0:
    print('Weird')
else:
    if n >= 2 & n <= 5:
        print('Not Weird')
    elif n >= 6 & n <= 20:
        print('Weird')
    else:
        print('Not Weird')
