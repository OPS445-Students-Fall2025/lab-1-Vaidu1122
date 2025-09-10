#!/usr/bin/env python3

# Name: Vaidehi Patel
# OPS 445 NDD
# Std ID: 166249219

# Lab 1 Script 4 - Lab 1 d

#print(10+5) #addition
#print(10-5) #substraction
#print(10*5) #multiplication
#print(10/5) #division
#print(10**5) #exponents

#print(5//2) #integer division
#print(5%2) #returns remainder of integer division

# Python follows PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Substraction)

#print(10+5*2) #multiplication happens before addition hence ans should be 20.
#print((10+5)*2) #parantheses happen before multiplication, hence ans should be 30.
#print(10+5*2-10**2) #first exponents, which makes 10**2 equals to 100, then multiplication, 5*2 = 10, hence, final equation would be, 10 + 10 - 100 = -80.
#print(15/3*4) # division and multiplication happen from left-to-right.
#print(100/((5+5)*2)) # the inner most parantheses first, so 5+5 = 10, the next outer paranthese, 10*2=20, then next outher parantheses, 100/20=5.

x = int(10)
y = int(2)
z = int(5)
solution = (x+y*z)

print(str(x) + ' + ' +  str(y) + ' * ' + str(z) + ' = ' + str(solution))
