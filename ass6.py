#1
import area
r = float(input("write  radius of circle  : "))
s = float(input("Enter side of square: "))
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
print("Area of Circle =", area.circle(r))
print("Area of Square =", area.square(s))
print("Area of Rectangle =",area.rectangle(l, b))
#2
file = open("sample.txt", "r")
vowels = 0
consonants = 0
for line in file:
    for ch in line.lower():
        if ch in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
file.close()
print("Frequency of Vowels =", vowels)
print("Frequency of Consonants =", consonants)
#3
file = open("sample.txt", "r")
content = file.read()
file.close()
mid = len(content) // 2
first_half = content[:mid]
second_half = content[mid:]
new_content = second_half + first_half
file = open("sample.txt", "w")
file.write(new_content)
file.close()
print("File content swapped successfully.")
print("New content:")
print(new_content)
#4
input_file = open("sample.txt", "r")
output_file = open("sample2.txt", "w")
for line in input_file:
    if line and line[0].islower():
        output_file.write(line)
input_file.close()
output_file.close()
print("Lines copied successfully to Demo2.txt")
#5
file = open("madlibs.txt", "r")
text = file.read()
file.close()
words = ["ADJECTIVE", "NOUN", "VERB", "NOUN"]
for word in words:
    while word in text:
        if word == "ADJECTIVE":
            replacement = input("Enter an adjective: ")
        elif word == "NOUN":
            replacement = input("Enter a noun: ")
        elif word == "ADVERB":
            replacement = input("Enter an adverb: ")
        elif word == "VERB":
            replacement = input("Enter a verb: ")
        text = text.replace(word, replacement, 1)
file = open("madlibs_output.txt", "w")
file.write(text)
file.close()
print("The following text file has been created:")
print(text)