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
import math 



q, r= mod(exp(array,sub(N,[1])),N)
        if (r == [1]):
            test1 = True
        else:
            test1 = False
    #if (test1):
     #   return True
    #else:
    #    return False
#
#    
#    for i in range(2,bin2dec(N)):
#        n = sub(N,[1])
#        a = exp(dec2bin(i),n)
#
#        if (Mod(bin2dec(a),bin2dec(N)) != 1):
#            print "Not a Prime"
#            return False
#    print "Number is Prime!"    
#    return True
#        
# x = Exp(a,N-1)
# if(mod(x,N) == 1):
#    return true
# return PrimalityTest(N)
#
   
def Primality2(N,k):
    x = primality2(dec2bin(N),k)
    return x

def spawnrandom(N):
    prime = []
    for i in range (N):
        x = randint(0,1)
        prime.append(x)
    print prime
    return prime 


if __name__ == "__main__":
#    while True:
#    PrimalityTest(16)
#    PrimalityTest(2)
#    PrimalityTest(23)
#    PrimalityTest(17)
#    PrimalityTest(997)
#    PrimalityTest(104729)
#    print(ExGCD(1273,941))
#    print(ExGCD(13,9))
    #        print(ExGCD(300,1321))
#    print(ExGCD(422,26424))
#    print(ExGCD(10,5))
#        print(ExGCD(17,33))
##        print(ExGCD(1273,941))
#        print(ExGCD(13,9))

    Primality2(13,10)
'''
while True:
option = int(raw_input("Enter option(1: test Problem3a, 2: test Problem3b, 3: quit): "))
if option == 3:
exit()
A, B, C, D = map(int, raw_input("Enter four numbers between 0 and 1000(separated by spaces): ").split())
if option == 1:
result = Problem3a(A, B, C, D)
print(result)
        if option == 2:
result = Problem3b(A, B, C, D)
print(result)
''' 
                   
        

        
