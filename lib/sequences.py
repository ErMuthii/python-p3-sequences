#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]

    for _ in range(length - 2):
        c = fibonacci_sequence[-2] + fibonacci_sequence[-1]
        fibonacci_sequence.append(c)

    return fibonacci_sequence


        
