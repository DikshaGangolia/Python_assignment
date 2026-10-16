# ques1
class Area:
    def calculate_area(self, a, b=None, shape="square"):
        if shape == "circle":
            return 3.14 * a * a
        elif b is None:
            return a * a
        else:
            return a * b
obj = Area()
print("Area of Square:", obj.calculate_area(5))
print("Area of Rectangle:", obj.calculate_area(10, 5))
print("Area of Circle:", obj.calculate_area(7, shape="circle"))

# ques2
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
def compare_marks(student1, student2):
    if student1.marks > student2.marks:
        print("Higher marks scored by:", student1.name)
    elif student2.marks > student1.marks:
        print("Higher marks scored by:", student2.name)
    else:
        print("Both students scored equal marks.")
# Create two student objects
s1 = Student("Aman", 101, 85)
s2 = Student("Riya", 102, 92)
# Display student details
s1.display()
print()
s2.display()
# Compare their marks
compare_marks(s1, s2)

# ques3
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return Complex(real_sum, imaginary_sum)
    def display(self):
        print(f"{self.real} + {self.imaginary}i")
# Create two complex number objects
c1 = Complex(3, 4)
c2 = Complex(2, 5)
# Add the objects using the + operator
c3 = c1 + c2
# Display the result
print("First complex number:")
c1.display()
print("Second complex number:")
c2.display()
print("Sum of complex numbers:")
c3.display()
