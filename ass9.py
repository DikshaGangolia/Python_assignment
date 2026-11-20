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
def validate_name(name):
    pattern = r'^[A-Za-z]{1,15}$'
    if re.fullmatch(pattern, name):
        return True
    else:
        return False
def validate_phone_no(phoneno):
    pattern = r'^[0-9]{10}$'
    if re.fullmatch(pattern, phoneno) and len(set(phoneno)) > 1:
        return True
    else:
        return False
def validate_email_id(email_id):
    pattern = r'^[A-Za-z0-9._%+-]+@(gmail|yahoo|hotmail)\.com$'
    if re.fullmatch(pattern, email_id):
        return True
    else:
        return False
name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email ID: ")
print("Name:", validate_name(name))
print("Phone Number:", validate_phone_no(phone))
print("Email ID:", validate_email_id(email))

# ques 3
import re
text = input("Enter the text: ")
text = text.lower()
words = re.findall(r'\b\w+\b', text)
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
result = max(frequency, key=lambda word: (frequency[word], len(word)))
print(result, frequency[result])

# ques 4
import re
def get_type(s):
    result = re.search(r"'([^']+)'", s)
    if result:
        return result.group(1)
print(get_type("<type 'int'>"))
print(get_type("<type 'float'>"))
print(get_type("<type 'builtin_function_or_method'>"))