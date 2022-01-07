#lambda function aka no name function or anonymous function
#lambda function can take any no. of arguments but only one expression
#using normal function we have to write more no of code than lambda function
x = lambda a:a+10
print(x(12))

y = lambda a, b :a+b
print(y(12,34))

z = lambda a,b,c:a+b+c
print(z(34,56,78))

# a is an argument and a+10 is an expression which got evaluated and returned.
x = lambda a:a+10
# Here we are printing the function object
print(x)
print("sum = ",x(20))