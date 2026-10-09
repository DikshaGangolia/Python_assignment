#  Implementation of print and input function in python
name = input("What's your name? ")
print("Welcome " + name + " to the training program on Artificial Intelligence and machine learning!")
city = input("Where are you from ?")
print("Nice to know that you come from " + city +  "!")
# Write a program to swap two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping:")
print("a =", a)
print("b =", b)
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)
#  Implementation of If else ladder
num = int(input("Enter a number: "))
if num > 0:
    print("Number is Positive")
else:
    print("Number is Not Positive")
# For loop with and Without range
for i in range(1, 6):
    print(i)
    name = "Diksha"
for ch in name:
    print(ch)