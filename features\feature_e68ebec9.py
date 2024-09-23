class Calculator:
    
    def __init__(self):
        pass
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2

# Example usage
calc = Calculator()
result_add = calc.add(5, 3)
result_subtract = calc.subtract(10, 4)
result_multiply = calc.multiply(2, 8)
result_divide = calc.divide(10, 2)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)