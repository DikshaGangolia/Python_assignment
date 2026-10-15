# ques1
class Instructor:
    def __init__(self):
        self.__name = ""
        self.__technology_skill = []
        self.__experience = 0
        self.__avg_feedback = 0.0
    def set_name(self, name):
        self.__name = name
    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill
    def set_experience(self, experience):
        self.__experience = experience
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback
    def check_eligibility(self):
        if self.__experience > 3:
            return self.__avg_feedback >= 4.5
        else:
            return self.__avg_feedback >= 4.0
    # Allocate course based on technology skill
    def allocate_course(self, technology):
        if self.check_eligibility() and technology in self.__technology_skill:
            return True
        return False
# Create instructor objects and initialize using setter methods
instructor1 = Instructor()
instructor1.set_name("Aman")
instructor1.set_technology_skill(["Python", "Java"])
instructor1.set_experience(5)
instructor1.set_avg_feedback(4.7)
instructor2 = Instructor()
instructor2.set_name("Riya")
instructor2.set_technology_skill(["C++", "Python"])
instructor2.set_experience(2)
instructor2.set_avg_feedback(4.2)
instructor3 = Instructor()
instructor3.set_name("Rahul")
instructor3.set_technology_skill(["Java", "SQL"])
instructor3.set_experience(6)
instructor3.set_avg_feedback(4.3)
# Test the methods
print("Anu eligible:", instructor1.check_eligibility())
print("Anu allocated Python:", instructor1.allocate_course("Python"))
print("Riya eligible:", instructor2.check_eligibility())
print("Riya allocated C++:", instructor2.allocate_course("C++"))
print("Bob eligible:", instructor3.check_eligibility())
print("Bob allocated Java:", instructor3.allocate_course("Java"))
print("Anu allocated python:", instructor1.allocate_course("python"))

# ques 2

class Bill:
    def __init__(self, bill_id, patient_name):
        self.bill_id = bill_id
        self.patient_name = patient_name
        self.bill_amount = 0
    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        total = consultation_fees
        for i in range(len(quantity_list)):
            total += quantity_list[i] * price_list[i]
        self.bill_amount = total
bill1 = Bill(101, "Aman Sharma")
bill1.calculate_bill_amount(500, [2, 3], [100, 50])
print("Bill ID:", bill1.bill_id)
print("Patient Name:", bill1.patient_name)
print("Bill Amount:", bill1.bill_amount)

# ques 3
class Apparel:
    counter = 100
    def __init__(self, price, item_type):
        Apparel.counter += 1
        self.__item_id = item_type[0].upper() + str(Apparel.counter)
        self.__price = price
        self.__item_type = item_type
    def calculate_price(self):
        self.__price += self.__price * 0.05
    def get_item_id(self):
        return self.__item_id
    def get_price(self):
        return self.__price
    def get_item_type(self):
        return self.__item_type
    def set_price(self, price):
        self.__price = price
class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, "Cotton")
        self.__discount = discount
    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        price -= price * self.__discount / 100
        price += price * 0.05
        self.set_price(price)
    def get_discount(self):
        return self.__discount
class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price, "Silk")
        self.__points = 0
    def calculate_price(self):
        super().calculate_price()
        if self.get_price() > 10000:
            self.__points = 10
        else:
            self.__points = 3
        price = self.get_price()
        price += price * 0.10
        self.set_price(price)
    def get_points(self):
        return self.__points
# Create objects
cotton1 = Cotton(2000, 10)
silk1 = Silk(12000)
silk2 = Silk(8000)
# Calculate final prices
cotton1.calculate_price()
silk1.calculate_price()
silk2.calculate_price()
# Display details
print("Cotton Apparel")
print("Item ID:", cotton1.get_item_id())
print("Item Type:", cotton1.get_item_type())
print("Discount:", cotton1.get_discount(), "%")
print("Final Price:", round(cotton1.get_price(), 2))
print("\nSilk Apparel")
print("Item ID:", silk1.get_item_id())
print("Item Type:", silk1.get_item_type())
print("Points:", silk1.get_points())
print("Final Price:", round(silk1.get_price(), 2))
print("\nSilk Apparel")
print("Item ID:", silk2.get_item_id())
print("Item Type:", silk2.get_item_type())
print("Points:", silk2.get_points())
print("Final Price:", round(silk2.get_price(), 2))

# ques4
class Shape:
    def __init__(self, color):
        self.color = color
class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        super().__init__(color)
        self.length = length
        self.breadth = breadth
    def calc_area(self):
        return self.length * self.breadth
class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    def calc_area(self):
        return 0.5 * self.base * self.height
rectangle = Rectangle("Blue", 10, 5)
triangle = Triangle("Red", 8, 6)
print("Rectangle Color:", rectangle.color)
print("Rectangle Area:", rectangle.calc_area())
print("Triangle Color:", triangle.color)
print("Triangle Area:", triangle.calc_area())
