class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
cal = Calculator()
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = input("Enter the operation (+, -, *, /): ")
if c == '+':
    result = cal.add(a, b)
elif c == '-':
    result = cal.subtract(a, b)
elif c == '*':
    result = cal.multiply(a, b)
elif c == '/':
    result = cal.divide(a, b)
else:
    result = "Invalid operation"
print(f"The result is: {result}")

