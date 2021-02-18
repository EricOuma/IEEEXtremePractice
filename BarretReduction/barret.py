#!usr/bin/python3

import random

def work(filename):
    with open(filename) as f:
        A, B = f.readline().split(' ')
    print(A, B)
    
work("input.txt")
