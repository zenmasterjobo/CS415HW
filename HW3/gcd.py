#!/usr/bin/env python
# Fern Vue
# Jordan Bergero

import random
import sys
import time

sys.setrecursionlimit(10000000)

from random import *

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

def fill(A, n):
    # adds n 0's at the end of the list A
    B = A[:]
    for j in range(n):
        B.append(0)
    return B

def complement(A):
    B = A[:]
    for j in range(len(B)):
        B[j] = 1 - B[j]
    return B

def exc_or(a, b, c):
    return (a ^ (b ^ c))
def nextcarry(a, b, c):
    if ((a & b) | (b & c) | (c & a)):
        return 1
    else:
        return 0 
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
def mod(A, B):
    (Q, R) = divide(A, B)
    return R

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
def divide(X, Y):
    # finds quotient and remainder when A is divided by B
    if zero(X):
        return ([],[])
    (q,r) = divide(div2(X), Y)
    q = add(q, q)
    r = add(r, r)
    if (not even(X)):
        r = add(r,[1])
    if (not compare(r,Y)== 2):
        r = sub(r, Y)
        q = add(q, [1])
    return (q,r)

def quotient(A, B):
    (Q, R) = divide(A, B)
    return Q

def bin2dec(A):
    if len(A) == 0:
        return 0
    val = A[0]
    pow = 2
    for j in range(1, len(A)):
        val = val + pow * A[j]
        pow = pow * 2
    return val

def compare(A, B):
    # compares A and B outputs 1 if A > B, 2 if B > A and 0 if A == B
    A1 = reverse(trim(A))
    A2 = reverse(trim(B))
    if len(A1) > len(A2):
        return 1
    elif len(A1) < len(A2):
        return 2
    else:
        for j in range(len(A1)):
            if A1[j] > A2[j]:
                return 1
            elif A1[j] < A2[j]:
                return 2
        return 0

def dec2bin(n):
    if n == 0:
        return []
    m = n/2
    A = dec2bin(m)
    fbit = n % 2
    return [fbit] + A

def sub(A, B):
    # returns 0 if A<= B, else returns A - B
    if (not (compare(A, B) == 1)):
        return []
    B1 = fill(B, len(A)-len(B))
    B1 = complement(B1)
    C = add(A, add(B1, [1]))
    return C[:len(C)-1]

# Binary representation of extended_GCD
def exGCD(A, B):
    if (zero(B)) :                          # Check if B is 0
        return [1], [], A, []                # Return (1,0,A)
    x, y, d, s = exGCD(B , mod(A,B))        # Recursive call with (x, y, GCD, sign)
    if(zero(x) or compare(s,[0,1]) == 2):
        # Check if x is zero. Since we need to subtract from this value 
        # it will be come a negative number, so we will add to it instead.
        s = [0,1]
        x = add(x,mult(quotient(A,B),y))
    elif(zero(y) or compare(s,[1]) == 1):
        # Check if y is zero. Since we need to subtract from this value 
        # it will be come a negative number, so we will add to it instead.
        # Otherwise, subtract x from the multiplication of y and the quotient of A,B.
        s = [1]
        x = add(x,mult(quotient(A,B),y))
    else:
        s = []
        x = sub(x,mult(quotient(A,B),y))
    return y, x, d, s                       # Return (y,x,d,s)

# Decimal representation of extended_GCD
def ExGCD(A, B):
    # Change input values to binary and then call binary extended_GCD
    x, y, d, s = exGCD(dec2bin(A),dec2bin(B))   
    # Return to caller decimal represntations of recieved binaries
    return bin2dec(x), bin2dec(y), bin2dec(d), bin2dec(s)

def gcd(A,B):
    if(zero(B)):
        return A
    return gcd(B,mod(A,B))

def GCD(A,B):
    return bin2dec(gcd(dec2bin(A),dec2bin(B)))

def fastGcd(a,b):
    if (compare(a,b) == 1):
        return fastGcd(b,a)
    if (compare(a,b) == 0):
        return a
    elif(even(a) and even(b)):
        return mult(fastGcd(div2(a),div2(b)),[0,1])
    elif(not even(a) and  even(b)):
        return fastGcd(a, div2(b))
    elif(even(a) and not even(b)):
        return fastGcd(div2(a),b)
    elif(not even(a) and not even(b) and (compare(a, b) == 1)):
        return fastGcd(div2(sub(a,b)), b)
    elif (not even(a) and not even(b) and (compare(a,b) == 2)):
        return fastGcd(a,div2(sub(b,a)))

def FastGCD(A,B):
    return bin2dec(fastGcd(dec2bin(A),dec2bin(B)))

if __name__ == "__main__":
    while True:
            A, B = map(int, raw_input("Enter two numbers for GCD (separated by spaces): ").split())
            t0 = time.time()
            d = GCD(A,B)
            print "Time for GCD: ", time.time() - t0, " GCD Answer: ", d
            t1 = time.time()
            e = FastGCD(A,B)
            print "Time for Divide And Conquer GCD: ", time.time() - t1, " Divide and Conquer Answer: ", e
            t2 = time.time()
            x,y,a,s = ExGCD(A,B)
            print "Time for Extended GCD: ", time.time() - t2, " Extended GCD Answer: ", a
