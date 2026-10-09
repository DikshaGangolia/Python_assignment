#  WAP to find the number of days in a month.
months = {"january": 31, "feburary": 28, "march": 31, "april": 30, "may": 31, "june": 30, "july": 31, "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}
x = input("Enter a month: ").lower()
if x in months:
    print(f"The number of days in {x} is {months[x]}.")
    n = input("Enter the number of rows: ")
''' WAP to display the pattern of numbers given as follows:
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1'''
for i in range(1, int(n) + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
for i in range(int(n) - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# WAP using while loop which prints sum of every fifth number from 0 to 500;
sum = 0
i = 0
while i <= 500:
    if i % 5 == 0:
        sum += i
    i += 1
print(sum)
# wap to display common character in the two strings
def common_charcter(str1 , str2):
    common_char =[]
    for char in str1:
        if char in str2 and char not in common_char:
            common_char.append(char)
    return common_char
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
case = common_charcter(str1, str2)
print(f"The common characters in the two strings are: {case}")
# 2.5
list1 = ['A','app','a','d','ke','th','doc','awa']
list2 = ['v','tor','e','eps','ay',None,'le','n']
reverse_list2 = list2[::-1]
for i in range(len(list1)):
        if reverse_list2[i] == None:
            print(list1[i] , end =" ")
        else:
            print(list1[i] + reverse_list2[i] , end =" ")