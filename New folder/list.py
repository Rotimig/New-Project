from typing import *
#object oriented project

fruitList = ["orange", "banana", "orange"]
anodaFruit: List = ["pear", "guava", "pineapple"]

def print_each_elem():
    fruitList.append(anodaFruit)
    for each_fruit in fruitList:
        print(each_fruit)


def print_elem_in_list():
    for each_fruit in fruitList:
        if type(each_fruit) != list:
            print(each_fruit)
        else:
            for wrapped_elem in each_fruit:
                print(wrapped_elem)


def print_range():
    number = range(5)
    print(number)
    for i in number:
        print(i)

