#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count) 
        count -= 1
    print("Happy New Year!")


def square_integers(int_list):
     
    sqrts = list()
    for numb in int_list: 
        sqrt = numb * numb
        sqrts.append(sqrt)
    return sqrts


def fizzbuzz():
    count = 0
    while count < 100: 
        count += 1
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        elif count % 5 == 0:
            print("Buzz")
        elif count % 3 == 0: 
            print("Fizz")
        else: 
            print(count)
