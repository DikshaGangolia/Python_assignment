# q1
spam = ['apples','bananas','tofu','cats']
def list_funct(list_value):
    if(len(list_value)==0):
        return ""
    elif(len(list_value)==1):
        return list_value[0]
    else:
        return ', '.join(list_value[:-1]) + ' and ' + list_value[-1];
list_value = print(list_funct(spam))
# q2
def calculate_bill_amount(gem_list,price_list,req_gem,req_quantity):
    bill_amount = 0
    if isinstance(req_gem, str):
        req_gem = [req_gem]
        req_quantity = [req_quantity]
    for gem, quantity in zip(req_gem, req_quantity):
        if gem not in gem_list:
            return -1
        index = gem_list.index(gem)
        bill_amount += price_list[index] * quantity
    if bill_amount > 30000:
        bill_amount -= bill_amount * 0.05
    return bill_amount
gem_list = ['Ruby', 'Emerald', 'Sapphire', 'Diamond']
price_list = [10000, 15000, 20000, 25000]
gemlist = [gem.lower() for gem in gem_list]
y = input("Enter the name of gem you want to purchase: ").strip().lower()
x = int(input("Enter the required amount of gem you want to purchase: "))
print(calculate_bill_amount(gemlist,price_list,y,x))
#q3
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', '.', '.'],
        ['.', '.', 'O', 'O', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for x in range(6):
    for y in range(9):
        print(grid[y][x], end='')
    print()
# q4
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
ans = []
if num1 < num2:
    for num in range(num1, num2 + 1):
        if 10 <= num <= 99:
            digit_sum = (num // 10) + (num % 10)
            if digit_sum % 3 == 0 and num % 5 == 0:
                ans.append(num)
if len(ans) == 0:
    print(-1)
else:
    print(max(ans))
# q5
def generate_ticket(passenger_count, source, destination):
    tickets = []
    if passenger_count <= 0:
        return tickets
    for i in range(passenger_count):
        ticket =  source[:3] + ":" + destination[:3] + ":" + str(101 + i)
        tickets.append(ticket)
    if passenger_count < 5:
        return tickets
    else:
        return tickets[-5:]
print(generate_ticket(8, "Delhi", "jaipur"))