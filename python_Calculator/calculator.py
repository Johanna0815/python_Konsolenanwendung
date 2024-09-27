class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def percentage(self, total, percent):
        return (total * percent) / 100


if __name__ == "__main__":
    calc = Calculator()
    print("Addition of 5 and 3:", calc.add(5, 3))
    print("10% of 50:", calc.percentage(50, 10))
