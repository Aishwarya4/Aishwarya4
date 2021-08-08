#Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.

# factorial of given number
# def factorial(n):
#     # single line to find factorial
#     return 1 if (n == 1 or n == 0) else n * factorial(n - 1);
#
# # Driver Code
# num = 8;
# print("Factorial of", num, "is",
#       factorial(num))

#using built in function
# factorial of given number
# import math
#
# def factorial(n):
# 	return(math.factorial(n))
#
#
# # Driver Code
# num = 7
# print("Factorial of", num, "is",
# 	factorial(num))

#using ternery operators
# def factorial(n):
#
# 	# single line to find factorial
# 	return 1 if (n==1 or n==0) else n * factorial(n - 1)
# # Driver Code
# num = 5
# print ("Factorial of",num,"is",
# 	factorial(num))

#using recursive method

def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);

# Driver Code
num = 5;
print("Factorial of", num, "is",
      factorial(num))


