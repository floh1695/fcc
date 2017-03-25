#!/usr/bin/env python3

for i in range(100):
    if i % 15 is 0:
        print('fizzbuzz')
    elif i % 5 is 0:
        print('buzz')
    elif i % 3 is 0:
        print('fizz')
    else:
        print(i)
