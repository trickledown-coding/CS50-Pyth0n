def main():
    
    prompt = input("Expression: ").split(" ")
    
    x = float(prompt[0])
    y = float(prompt[2])
    op = prompt[1]

    

    if op  == "+":
        print(add(x, y))
    elif op == "-":
        print(subtract(x, y))
    elif op == "*":
        print(multiply(x, y))
    elif op == "/":
        print(divide(x, y))


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


main() 