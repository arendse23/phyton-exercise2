# Arithmetic and Assignment Operators
x = 20
x += 3
print(x)
# Output: 23

y = 15
y *= 2
print(y)
# Output: 30

result = x / y
print(result)
# output: 0.8333333333333334

# comparison and logical operators
a = 18
b = 20
c = 19

condition_1 = a > b

condition_2 = b % 2 == 0

condition_3 = c <= a

final_condition = condition_1 or (condition_2 and condition_3)
print(final_condition)
#output : False

# conditional statements
score = int(input("Enter your score: "))
if score >= 90:
    grade= "A"
elif score >= 80:
    grade= "B"
elif score >= 70:
    grade= "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"grade: {grade}")

# Combining operators and conditionals
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 -num2

elif operator == '*':
    result = num1 * num2

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero")
        result = None

else:
    print("Invalid operation selected!")

if result is not None:
    print(result)



