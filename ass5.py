#1.
t = (10, "apple", 3.5, 20, "banana", True, 7.2, False, "cat")
integers = tuple(x for x in t if type(x) == int)
strings = tuple(x for x in t if type(x) == str)
floats = tuple(x for x in t if type(x) == float)
booleans = tuple(x for x in t if type(x) == bool)
grouped_tuple = (
    tuple(sorted(integers)),
    tuple(sorted(strings)),
    tuple(sorted(floats)),
    tuple(sorted(booleans))
)
print("Larger tuple:", grouped_tuple)
print("Integers:", grouped_tuple[0])
print("Strings:", grouped_tuple[1])
print("Floats:", grouped_tuple[2])
print("Booleans:", grouped_tuple[3])
#2
list = ["apple", "banana","cherry", "orange","grapes"]
result = {}
for s in list:
    result[s] = len(s)
print("Dictionary:", result)
#3
def find_max_speciality(patient_list):
    speciality = {
        "P": "Pediatrics",
        "O": "Orthopedics",
        "E": "ENT"
    }
    count = {}
    for i in range(1, len(patient_list), 2):
        code = patient_list[i]
        count[code] = count.get(code, 0) + 1
    max_code = max(count, key=count.get)
    return speciality[max_code]
patient_list = [101, "P", 102, "O", 302, "P", 305, "P"]
print(find_max_speciality(patient_list))
#4
def find_correct(answer_dict):
    correct = 0
    almost_correct = 0
    wrong = 0
    for correct_word, contestant_word in answer_dict.items():
        if correct_word == contestant_word:
            correct += 1
        elif len(correct_word) != len(contestant_word):
            wrong += 1
        else:
            differences = 0
            for i in range(len(correct_word)):
                if correct_word[i] != contestant_word[i]:
                    differences += 1
            if differences <= 2:
                almost_correct += 1
            else:
                wrong += 1
    return [correct, almost_correct, wrong]
answers = {
    "HELLO": "HELLO",
    "WORLD": "WORLF",
    "PYTHON": "PITHON",
    "COMPUTER": "COMPTER",
    "APPLE": "AP"
}
print(find_correct(answers))
#5
def tr(srcstr, dststr, string):
    result = ""
    for ch in string:
        if ch in srcstr:
            index = srcstr.index(ch)
            result += dststr[index]
        else:
            result += ch
    return result
def tr_delete(srcstr, dststr, string):
    result = ""
    for ch in string:
        if ch in srcstr:
            index = srcstr.index(ch)
            if index < len(dststr):
                result += dststr[index]
        else:
            result += ch
    return result
print("Part (a):", tr("abc", "mno", "abcdef"))
print("Part (b):", tr_delete("abcdef", "mno", "abcdefghi"))