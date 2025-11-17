def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "error can't devide by 0"
    return a/b

print("simple calculeter")
print("opraters +, -, *, /")

a = float(input("enter 1st number: "))
op = input("inter operator: ")
b = float(input("enter 2nd number: "))

if op == "+":
    result = add(a,b)
elif op == "-":
    result = subtract(a,b)
elif op == "*":
    result = multiplication(a,b)
elif op == "/":
    result = divide(a,b)
else:
    result = "invelid oprator"

print("result", result)