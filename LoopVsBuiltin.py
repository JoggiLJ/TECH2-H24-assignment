#!/usr/bin/env python3

import numpy as np
from math import sqrt

def std_loops(x):
    
    # Define the veriables that are used in the loop
    # After experimenting I found out that I had to define values like 'total' and 'length' to use loops for this assignment
    length = 0
    mean = 0
    mean_square = 0
    variance = 0
    total = 0
    total_square = 0
    
    for i in x:
        length = length + 1
        total = total + i
        mean = total/length
        total_square = total_square + i**2
        mean_square = total_square/length
        variance = mean_square - mean**2
        
        sd1 = sqrt(variance)
        
        # I put all the operations inside the for loop, even though that isnt really necessary
        # that is however, how i read the assignment, and my 'coworkers' way of doing this...
        
    return sd1
    
def std_builtin(x):
    
    # I defina an empty list x2, similarly to how I defined lenght to 0 in the previous function
    x2 = []
    mean = sum(x)/len(x)
    
    for i in x:
        x2.append(i**2)
        
    # Im not sure if i could do this without a for loop, but I have at least minimized the use of them in this option 
        
    mean_square = sum(x2)/len(x)
    variance = mean_square - mean**2
    
    sd2 = sqrt(variance)
    
    return sd2
    
def main():
    
    # I define the main function, and put the relevant list x inside the main function
    
    x = [1, 2, 3, 4, 5]
    
    sd1 = std_loops(x)
    
    sd2 = std_builtin(x)
    
    sd3 = np.std(x)
    
    print(f'The first method gives us the result {sd1:.4f}. \nThe second method gives us the result {sd2:.4f}. \nAnd the third method gives us the result {sd3:.4f} \nThey all approximatley give the same result')

main()
# I run the main funcion

