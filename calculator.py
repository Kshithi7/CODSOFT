def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
     return "divisor cannot be zero"
    return a/b

print("Welcome to simple calculator!")
print("perform desired operation")

x = float(input("Enter first number:"))
y = float(input("Enter second number:"))

print("Enter operation to be performed:")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")
op = input ("Your choice: ")

if op == "1":
  answer= add(x,y)
elif op == "2":
  answer= sub(x,y)
elif op == "3":
  answer= mul(x,y)
elif op == "4":
  answer= div(x,y)
else: 
  answer="Operation not found!"

print("Answer:",answer)
