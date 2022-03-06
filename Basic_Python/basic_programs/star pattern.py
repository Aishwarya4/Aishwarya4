# User input for number of rows
rows = int(input("Enter the rows:"))
# Outer loop will print number of rows
for i in range(0,rows+1):
# Inner loop will print number of Astrisk
    for j in range(i):
        print("*",end = '')
    print()

rows = int(input("Enter the rows"))
for i in range(0,rows+1):
    for j in range(i):
        print(i,end = '')
    print()

    # Python 3.x code to demonstrate star pattern

    # Function to demonstrate printing pattern
    def pypart(n):

        # outer loop to handle number of rows
        # n in this case
        for i in range(0, n):

            # inner loop to handle number of columns
            # values changing acc. to outer loop
            for j in range(0, i + 1):
                # printing stars
                print("* ", end="")

            # ending line after each row
            print("\r")
    # Driver Code
    n = 5
    pypart(n)


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def numpat(n):
    # initialising starting number
    num = 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # re assigning num
        num = 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing number
            print(num, end=" ")

            # incrementing number at each column
            num = num + 1

        # ending line after each row
        print("\r")
# Driver code
n = 5
numpat(n)


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def alphapat(n):
    # initializing value corresponding to 'A'
    # ASCII value
    num = 65

    # outer loop to handle number of rows
    # 5 in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # explicitly converting to char
            ch = chr(num)

            # printing char value
            print(ch, end=" ")

        # incrementing number
        num = num + 1

        # ending line after each row
        print("\r")


# Driver Code
n = 5
alphapat(n)



# Python code 3.x to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def contalpha(n):
    # initializing value corresponding to 'A'
    # ASCII value
    num = 65


# outer loop to handle number of rows

for i in range(0, n):

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
        # explicitly converting to char
        ch = chr(num)

        # printing char value
        print(ch, end=" ")

        # incrementing at each column
        num = num + 1

    # ending line after each row
    print("\r")

# Driver code
n = 5
contalpha(n)
