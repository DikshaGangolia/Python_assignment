# ques 1
import re
poem = """If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain."""
# 1. Count the number of times 'v' appears
count = len(re.findall(r'v', poem))
print(count)
# 2. Remove all newlines and print in a single line
single_line = re.sub(r'\n', ' ', poem)
print(single_line)
# 3. Replace 'ch' with 'Ch' and 'co' with 'Co'
result = re.sub(r'ch', 'Ch', poem)
result = re.sub(r'co', 'Co', result)
print(result)
# 4. Replace the next three characters after 'ai' or 'hi' with *\*
result = re.sub(r'(ai|hi)...', r'\1*\\*', poem)
print(result)

# ques 2
import re
# Function to validate name
def validate_name(name):
    pattern = r'^[A-Za-z]{1,15}$'
    if re.fullmatch(pattern, name):
        return True
    else:
        return False
# Function to validate phone number
def validate_phone_no(phoneno):
    pattern = r'^[0-9]{10}$'
    if re.fullmatch(pattern, phoneno) and len(set(phoneno)) > 1:
        return True
    else:
        return False
# Function to validate email ID
def validate_email_id(email_id):
    pattern = r'^[A-Za-z0-9._%+-]+@(gmail|yahoo|hotmail)\.com$'
    if re.fullmatch(pattern, email_id):
        return True
    else:
        return False
# Taking input from user
name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email ID: ")
# Displaying validation results
print("Name:", validate_name(name))
print("Phone Number:", validate_phone_no(phone))
print("Email ID:", validate_email_id(email))

# ques 3
import re
text = input("Enter the text: ")
# Convert text into lowercase
text = text.lower()
# Extract all words using regular expression
words = re.findall(r'\b\w+\b', text)
# Dictionary to store word frequencies
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
# Find the word with maximum frequency
result = max(frequency, key=lambda word: (frequency[word], len(word)))
print(result, frequency[result])

# ques 4
import re
def extract_type(type_string):
    pattern = r"<type '([^']+)'>"
    result = re.search(pattern, type_string)
    if result:
        return result.group(1)
    else:
        return None
# Testing the function
print(extract_type("<type 'int'>"))
print(extract_type("<type 'float'>"))
print(extract_type("<type 'builtin_function_or_method'>"))
print(extract_type("<type 'str'>"))