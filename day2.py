# Calculator


def add(numb1, numb2):
    return numb1 + numb2

def subtract(numb1, numb2):
    return numb1 - numb2

def multiply(numb1, numb2):
    return numb1 * numb2

def divide(numb1, numb2):
    return numb1 / numb2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = float(input("What is your first number?: "))

for symbol in operations:
    print(symbol)

operation = input("What operation do you want to perform: ")

num2 = float(input("What is your second number? "))

answer = (operations[operation](num1, num2))

print(f"{num1} {operation} {num2} = {answer}")