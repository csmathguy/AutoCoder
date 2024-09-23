{
    "file": "calculator.py",
    "type": "create",
    "location": "Calculator",
    "code": "
class Calculator:
    def add(self, num1, num2):
        \"\"\"Add two numbers and return the result.\"\"\"
        return num1 + num2

    def subtract(self, num1, num2):
        \"\"\"Subtract num2 from num1 and return the result.\"\"\"
        return num1 - num2

    def multiply(self, num1, num2):
        \"\"\"Multiply two numbers and return the result.\"\"\"
        return num1 * num2

    def divide(self, num1, num2):
        \"\"\"Divide num1 by num2 and return the result.\"\"\"
        if num2 == 0:
            raise ValueError('Cannot divide by zero')
        return num1 / num2
"
}