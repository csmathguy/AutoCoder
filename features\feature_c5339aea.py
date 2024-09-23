{
    "file": "calculator.py",
    "type": "create",
    "location": "Calculator",
    "code": "class Calculator:\n\\n    def add(self, a, b):\n        '''Add two numbers'''\\n        return a + b\n\\n    def subtract(self, a, b):\n        '''Subtract two numbers'''\\n        return a - b\n\\n    def multiply(self, a, b):\n        '''Multiply two numbers'''\\n        return a * b\n\\n    def divide(self, a, b):\n        '''Divide two numbers'''\\n        if b == 0:\n            raise ValueError('Cannot divide by zero')\n        return a / b"
}