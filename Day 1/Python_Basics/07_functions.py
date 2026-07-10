# Function

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# Function with default argument

def greet(name="Student"):
    print("Hello", name)

greet()

greet("Roshani")

# Lambda Function

multiply = lambda x, y: x * y

print(multiply(5, 6))