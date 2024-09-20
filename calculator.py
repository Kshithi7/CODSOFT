
# Define the arthmetic operations
def add(a,b):  # addition
    return a+b
def sub(a,b):  # subtraction
    return a-b
def mul(a,b):  # multiplication
    return a*b
def div(a,b):   # division
    if b==0:
     return "divisor cannot be zero" # mathematical error
    return a/b


# Display in-app messages
print("Welcome to simple calculator!")
print("perform desired operation")

# User input
x = float(input("Enter first number:"))
y = float(input("Enter second number:"))

# Display the menu
print("Enter operation to be performed:")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")
op = input ("Your choice: ")

# Call the  desired defined functions 
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

# print the answer
print("Answer:",answer)