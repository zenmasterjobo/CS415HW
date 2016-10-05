# implements most of the functions described in Ch 1 of Das Gupta et al.'s
# algorithms book We do not use the unlimited size integer implementation of Python
# except in: bin2dec(), dec2bin() functions
# most functions with upper-case first letter take decimal inputs and produce
# decimal outputs.
# only the main arithmetic functions are provided with decimal interface
# supporting functions with deal with binary inputs/outputs
# supporting functions (such as shift, div2 etc.) only have a binary version

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

def Compare(A, B):
    return bin2dec(compare(dec2bin(A), dec2bin(B)))

def exp(A, B):
    if zero(B):
        return [1]
    else:
        A1 = mult(A, A)
        B1 = div2(B)
        if even(B):
            return exp(A1, B1)
        else:
            return mult(A, exp(A1, B1))

def Exp(A, B):
    return bin2dec(exp(dec2bin(A), dec2bin(B)))

def mod(A, B):
    (Q, R) = divide(A, B)
    return R

def Mod(A, B):
    return bin2dec(mod(dec2bin(A), dec2bin(B)))

def quotient(A, B):
    (Q, R) = divide(A, B)
    return Q

def Quotient(A, B):
    return bin2dec(quotient(dec2bin(A), dec2bin(B)))

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

def complement(A):
    B = A[:]
    for j in range(len(B)):
        B[j] = 1 - B[j]
    return B
    
def sub(A, B):
    # returns 0 if A<= B, else returns A - B
    if (not (compare(A, B) == 1)):
        return []
    B1 = fill(B, len(A)-len(B))
    B1 = complement(B1)
    C = add(A, add(B1, [1]))
    return C[:len(C)-1]

def Sub(A, B):
    # this function calls sub(A, B). if A <= B, sub will return 0 so
    # in this case, this function will return A - B correctly by exploiting the
    # unlimited precision arithmetic support of Python. Although this violates
    # the goal of this project (namely not to rely on Python's unlimited precision
    # built-in arithmetic, just returning a string by concatenating - symbol to
    # the string rep of the output will cause problems when the output of Sub is
    # used as input to other functions (e.g. in the case of GCD, EGCD etc.)
    temp1 = bin2dec(sub(dec2bin(A), dec2bin(B)))
    temp2 = bin2dec(sub(dec2bin(B), dec2bin(A)))
    if A > B:
        return temp1
    else:
        return -temp2
    
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

def Divide(X, Y):
    p, q = divide(dec2bin(X), dec2bin(Y))
    return bin2dec(p), bin2dec(q)


def Problem3a(A, B, C, D):
    '''
    Input: four integers A, B, C, D such that 0 < A, B, C, D < 1000
    Output: A^B - C^D
    '''
    return Sub(Exp(A, B), Exp(C, D))

def findNeg(A,B):
    return sub(A,B)

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
    
def modInv(A,B):
    x, y, d, s = exGCD(A,B)
    if(compare(d,[1]) == 0):
        if(compare(s,[1]) == 0):
            if(compare(x,B) == 1):
                # The inverse is a negative number > B
                while(compare(x,B) == 1):
                    c = sub(x,B)
                    if(compare(c,[])== 0):
                        x = (B,x)
            else:
                # The inverse is a negative number < B
                x = sub(B,x)
            return x
        return x # The inverse is a postive number.
    return [] # There is no modular inverse for the two passed numbers.

# Return the decimal form of the binary representation for modular
# inverse.
def ModInv(A,B):
    x = modInv(dec2bin(A),dec2bin(B))
    return bin2dec(x)

def Problem3b(A, B, C, D):
    '''
    Input: four integers A, B, C, D such that 0 < A, B, C, D < 1000
    Output: quotient and remainder when A^B is divided by C^D
    '''
    P = Exp(A, B)
    Q = Exp(C, D)
    return Divide(P, Q)

def primality2(N,k):
    for i in range (k):
        a = randomNumber(len(N))
        if(compare(modExp(a,sub(N,[1]),N), [1]) != 0):
            return False
    return True
   
def Primality2(N,k):
    x = primality2(dec2bin(N),k)
    return x

def randomNumber(N):
    num = [1]
    for i in range (N):
        num.append(randint(0,1))
    num.append(1)
    return num

def modExp(x,y,N):
    if(zero(y)):
        return [1]
    z = modExp(x,y[1:],N)
    if (y[0] == 0):
        return mod(mult(z,z),N)
    else:
        return mod(mult(x,mult(z,z)),N)

def ModExp(A,e,M):
    return bin2dec(modExp(dec2bin(A),dec2bin(e),dec2bin(M)))
    
def RSAKeyGenerate(N,C):
    x = 0
    while(True):
        x = bin2dec(randomNumber(N))
        if(x != 0):
            if(Primality2(x,C)):
                if(Mod(x,3) == 2):
                    p = x
                    break
    while(True):
        y = bin2dec(randomNumber(N))
        if(y != 0):
            if(Primality2(y,C)):
                if(Mod(y,3) == 2 and y != x):
                    q = y
                    break

    n = mult(dec2bin(p),dec2bin(q))
    e = 3
    d = RSACreateD(p, q, e)
    return bin2dec(n), p, q, d, e

def RSAencrypt(M,e,N):
    return modExp(M,e,N)

def RSAEncrypt(M,e,N):
    return bin2dec(RSAencrypt(dec2bin(M),dec2bin(e),dec2bin(N)))
    
def RSAdecrypt(E,d,N):
    return modExp(E,d,N)

def RSADecrypt(E,d,N):
    return bin2dec(RSAdecrypt(dec2bin(E),dec2bin(d),dec2bin(N)))

def RSAcreateD(P,Q,e):
    return modInv(e,mult(sub(P,[1]),sub(Q,[1])))

def RSACreateD(P,Q,e):
    return bin2dec(RSAcreateD(dec2bin(P),dec2bin(Q),dec2bin(e)))

if __name__ == "__main__":
    while True:
        option = int(raw_input("Enter option (1: test extended GCD, 2: test primality, 3: test RSA key generate,\n 4: test RSA-encrypt and RSA-decrypt, 5: exit ): "))
        if option == 5:
             exit()
        if option == 1:
            A, B = map(int, raw_input("Enter two numbers for extended GCD (separated by spaces): ").split())
            result = ExGCD(A,B)
            print(result)
        if option == 2:
            A, B = map(int, raw_input("Enter two numbers for primality (N,k) (separated by spaces): ").split())
            result = Primality2(A,B)
            print(result)
        if option == 3:
            A = int(raw_input("Enter a bit length to create two primes with that length and a RSA public key: "))
            C = int(raw_input("enter a number for confidence: "))
            N,P,Q,d,e = RSAKeyGenerate(A,C)
            print "Public Key:", N , " P: ", P ," Q:", Q , "D:", d , "e:", e
        if option == 4:
            M = int(raw_input("Enter a message to encode (Will also show decrypted message): "))
            E = RSAEncrypt(M,3,N)
            print "Encrypted Message: ", E
            result = RSADecrypt(E,d,N)
            print "Decrypted Message: ", result
