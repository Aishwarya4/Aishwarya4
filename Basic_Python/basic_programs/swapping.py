#1)
# Python code to swap two numbers
# without using another variable
# x = 5
# y = 7
#
# print ("Before swapping: ")
# print("Value of x : ", x, " and y : ", y)
#
# # code to swap 'x' and 'y'
# x, y = y, x
#
# print ("After swapping: ")
# print("Value of x : ", x, " and y : ", y)


#2)
# Python code to swap two numbers
# using Bitwise XOR method

# x = 95 # x = 0101
# y = 50 # y = 1010
#
# print ("Before swapping: ")
# print("Value of x : ", x, " and y : ", y)
#
# # Swap code
# x ^= y # x = 1111, y = 1010
# y ^= x # y = 0101, x = 1111
# x ^= y # x = 1010, y = 0101
#
# # print ("After swapping: ")
# print("Value of x : ", x, " and y : ", y)

#3)
# Python code to swap two numbers
# using + and - operators
# x = 5.4
# y = 10.3
#
# print ("Before swapping: ")
# print("Value of x : ", x, " and y : ", y)
#
# # Swap code
# x = x + y # x = 15.7, y = 10.3
# y = x - y # x = 15.7, y = 5.4
# x = x - y # x = 10.3, y = 5.4
#
# print ("After swapping: ")
# print("Value of x : ", x, " and y : ", y)

#4)
# Python code to swap two numbers
# using / and * operators
# x = 5.4
# y = 10.3
#
# print ("Before swapping: ")
# print("Value of x : ", x, " and y : ", y)
#
# # Swap code
# x = x * y # x = 55.62, y = 10.3
# y = x / y # x = 55.62, y = 5.4
# x = x / y # x = 10.3, y = 5.4
#
# print ("After swapping: ")
# print("Value of x : ", x, " and y : ", y)

#5)
# python program to swap two numbers
# # using bitwise addition for swapping
# x = 50;
# y = 10;
#
# print ("Before swapping: ") ;
# print("Value of x : ", x, " and y : ", y) ;
#
# # same as x = x + y
# x = (x & y) + (x|y) ;
#
# #vsame as y = x - y
# y = x + (~y) + 1 ;
#
# # same as x = x - y
# x = x + (~y) + 1 ;
#
# print ("After swapping: ")
# print("Value of x : ", x, " and y : ", y)

#6)
# Python program to demonstrate
# swapping of two variables

# x = 10
# y = 50
#
# # Swapping of two variables
# # Using third variable
# temp = x
# x = y
# y = temp
#
# print("Value of x:", x)
# print("Value of y:", y)


#7)
# python 3 program to swap three variables
# without using temporary variable.

# Assign c's value to a, a's value to b and
# b's value to c.
def swapThree(a, b, c):
    # Store sum of all in a
    a = a + b + c  # (a = 60)

    # After this, b has value of a
    b = a - (b + c)  # (b = 60 – (20+30) =10)

    # After this, c has value of b
    c = a - (b + c)  # (c = 60 – (10 + 30) = 20)

    # After this, a has value of c
    a = a - (b + c)  # (a = 60 – (10 + 20) = 30)

    print("After swapping a =", a, ", b =", b, ", c =", c)


# Driver code
if __name__ == '__main__':
    a = 10
    b = 20
    c = 30

    print("Before swapping a =", a, ", b =", b, ", c =", c)

    swapThree(a, b, c)

# This code is contributed by
# Surendra_Gangwar

