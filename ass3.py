 # 3.1
string = input("enter a string:");
def string_count(string):
    string_new = "";
    count =1
    for i  in range(len(string)-1):
        if(string[i] == string[i+1] ):
            count+=1;
        else:
            string_new+= str(count) + string[i];
            count = 1
    string_new += str(count) +string[-1];
    return string_new;
print(string_count(string));
# QUESTION 2
def find_pairs_of_numbers(numbers , target):
    count = 0;
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1):
            if(numbers[i] + numbers[j] == target):
                count+=1;
    return count;
print(find_pairs_of_numbers([1,2,3,4,5,6],9))
# question 3
marks = (12, 18, 20, 15, 18, 10, 25, 20, 18, 14)
def find_more_than_average():
    average = sum(marks) / len(marks)
    count = 0
    for mark in marks:
        if mark > average:
            count += 1
    percentage = (count / len(marks)) * 100
    return percentage
def generate_frequency():
    frequency = [0] * 26
    for mark in marks:
        frequency[mark] += 1
    return frequency
def sort_marks():
    sorted_marks = list(marks)
    sorted_marks.sort()
    return sorted_marks
print("Percentage above average:", find_more_than_average())
print("Frequency:", generate_frequency())
print("Sorted marks:", sort_marks())
# question 4
sample_data = range(1, 11)
def odd():
    result = []
    for i in sample_data:
        if i % 2 != 0:
            result.append(i)
    return result
def even():
    result = []
    for i in sample_data:
        if i % 2 == 0:
            result.append(i)
    return result
def sum_of_numbers(function=None):
    if function is None:
        total = 0
        for i in sample_data:
            total = total + i
        return total
    else:
        numbers = function()
        total = 0
        for i in numbers:
            total = total + i
        return total
print("Odd numbers:", odd())
print("Even numbers:", even())
print("Sum of all numbers:", sum_of_numbers())
print("Sum of odd numbers:", sum_of_numbers(odd))
print("Sum of even numbers:", sum_of_numbers(even))
# question 5
def check_anagram(string1, string2):
    str1 = string1.lower()
    str2 = string2.lower()
    if(len(str1) != len(str2)):
        return False;
    if(sorted(str1) == sorted(str2)):
        if(string1[0] != string2[0]):
            return True;
    else:
        return False;
enter_string1 = input("Enter first string: ")
enter_string2 = input("Enter second string: ")
print(check_anagram(enter_string1, enter_string2))