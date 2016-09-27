# implementation of the algorithms for addition and multiplication in binary
# we use python's unlimited precision arithmetic in the two functions dec2bin and bin2dec
# works with Python 2.7, not Python 3.*
# Authors:
# Jordan Bergero
# Fern Vue
#
#
#

import random
import sys
import time

sys.setrecursionlimit(10000000)

from random import *

def shift(A, n):
    if n == 0:
        return A
    return [0]+shift(A, n-1)
    
def mult(X, Y):
    # mutiplies two arrays of binary numbers
    # with LSB stored in index 0
    if zero(Y):
        return [0]
    Z = mult(X, div2(Y))
    if even(Y):
        return add(Z, Z)
    else:
        return add(X, add(Z, Z))

def Mult(X, Y):
    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(mult(X1,Y1))

def zero(X):
    # test if the input binary number is 0
    # we use both [] and [0, 0, ..., 0] to represent 0
    if len(X) == 0:
        return True
    else:
        for j in range(len(X)):
            if X[j] == 1:
                return False
    return True

def div2(Y):
    if len(Y) == 0:
        return Y
    else:
        return Y[1:]

def even(X):
    if ((len(X) == 0) or (X[0] == 0)):
        return True
    else:
        return False

def add(A, B):
    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)
    if n < m:
        for j in range(len(B1)-len(A1)):
            A1.append(0)
    else:
        for j in range(len(A1)-len(B1)):
            B1.append(0)
    N = max(m, n)
    C = []
    carry = 0
    for j in range(N):
        C.append(exc_or(A1[j], B1[j], carry))
        carry = nextcarry(carry, A1[j], B1[j])
    if carry == 1:
        C.append(carry)
    return C

def Add(A,B):
    return bin2dec(add(dec2bin(A), dec2bin(B)))

def exc_or(a, b, c):
    return (a ^ (b ^ c))

def nextcarry(a, b, c):
    if ((a & b) | (b & c) | (c & a)):
        return 1
    else:
        return 0 
        
def bin2dec(A):
    if len(A) == 0:
        return 0
    val = A[0]
    pow = 2
    for j in range(1, len(A)):
        val = val + pow * A[j]
        pow = pow * 2
    return val

def reverse(A):
    B = A[::-1]
    return B

def trim(A):
    if len(A) == 0:
        return A
    A1 = reverse(A)
    while ((not (len(A1) == 0)) and (A1[0] == 0)):
        A1.pop(0)
    return reverse(A1)

def dec2bin(n):
    if n == 0:
        return []
    m = n/2
    A = dec2bin(m)
    fbit = n % 2
    return [fbit] + A

def fill(A, n):
    # adds n 0's at the end of the list A
    B = A[:]
    for j in range(n):
        B.append(0)
    return B

# this function divides two decimal numbers
def divide(A,B):
    if A == 0:
        return (0,0)
    (q,r) = divide(A//2,B)
    q = 2 * q
    r = 2 * r
    if A%2 == 1:
        r = r+1
    if r >= B:
        r = r - B
        q = q + 1
    return (q,r)

# this function raises the passed value A, to the value B
def exponent(A, B):
    e = 1
    if B == 0:
        return 1
    for j in range (B):
        e = Mult(e,A)
    return e

# this function returns the two's compliment of a passed list
def twoComp(B):
    for j in range (len(B)):
        if B[j] == 0:
            B[j] = 1
        else:
            B[j] = 0
    B = add(B,[1])
    return B

# this function subtracts two binary lists of numbers.
def subtract(A, B):
    if len(B) == 0:
        return A   
    n = len(A)
    m = len(B)
    A1 = A[:]
    B1 = B[:]
    if n < m:
        for j in range(len(B)-len(A)):
            A.append(0)
    else:
        for j in range(len(A)-len(B)):
            B.append(0)
    B = twoComp(B)
    C = add(A,B)
    if(bin2dec(A1) < bin2dec(B1)):
        C = twoComp(C)
        return int('-' + str(bin2dec(C)))
    else:
        C.pop();
        return bin2dec(C)

def problem3a(A,B,C,D):
    E = exponent(A,B)
    F = exponent(C,D)
    print("3a Solution: ", subtract(dec2bin(E),dec2bin(F)))

def problem3b(A,B,C,D):
    E = exponent(A,B)
    F = exponent(C,D)
    print("3b Solution", divide(E,F))
    
    


    
def main():
    x = 1
    while (x != "q"):
        x = raw_input("Enter 1 to test 3a or Enter 2 to test 3b or q to quit: ")
        if (x == "q"):
            sys.exit(1)
        if (x == "1"):
            user_input = [x for x in raw_input("Enter 4 Numbers 0 < A,B,C,D < 1000 (Comma delimited): ").split(',')]
            a = int(user_input[0])
            b = int(user_input[1])
            c = int(user_input[2])
            d = int(user_input[3])
            if(a < 1 or a > 1000):
                print ("Please enter a valid number for A. ")
                a = input("Enter a number 0 < A < 1000: ") 
            if(b < 1 or b > 1000):
                print ("Please enter a valid number for B. ")
                b = input("Enter a number 0 < B < 1000: ")
            if(c < 1 or c > 1000):
                print ("Please enter a valid number for C. ")
                c = input("Enter a number 0 < C < 1000: ")
            if(d < 1 or d > 1000):
                print ("Please enter a valid number for D. ")
                d = input("Enter a number 0 < D < 1000: ")
            problem3a(a,b,c,d) 
        if(x == "2"):
            user_input = [x for x in raw_input("Enter 4 Numbers 0 < A,B,C,D < 1000 (Comma delimited): ").split(',')]
            a = int(user_input[0])
            b = int(user_input[1])
            c = int(user_input[2])
            d = int(user_input[3])
            if(a < 1 or a > 1000):
                print ("Please enter a valid number for A. ")
                a = input("Enter a number 0 < A < 1000: ") 
            if(b < 1 or b > 1000):
                print ("Please enter a valid number for B. ")
                b = input("Enter a number 0 < B < 1000: ")
            if(c < 1 or c > 1000):
                print ("Please enter a valid number for C. ")
                c = input("Enter a number 0 < C < 1000: ")
            if(d < 1 or d > 1000):
                print ("Please enter a valid number for D. ")
                d = input("Enter a number 0 < D < 1000: ")
            problem3b(a,b,c,d) 
       
            
        #print("Division ",divide(x,y))
        #print("Exponent ",exponent(x,y))
        #print("Subtraction ", subtract(dec2bin(x),dec2bin(y)))
main()

