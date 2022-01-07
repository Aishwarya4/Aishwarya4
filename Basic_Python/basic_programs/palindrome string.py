# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")

# Python program to check if a string is palindrome or not
x = "malayalam"
w = ""
for i in x:
	w = i + w

if (x == w):
	print("Yes")
else:
	print("No")

# Python program to check if a number is palindrome or not
num = input("Enter a number: ")
if num == num[::-1]:
	print("Yes its a palindrome")
else:
	print("No, its not a palindrome")
