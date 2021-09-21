# Python Program 01 - Calculator (ENGR4)
#Written by Sean Lynch
#9.14.2021

# These two lines ask the user whatever is inside the quotation markes and then
# takes their response and makes that the a or b variable. Because you have a/b
# equals to int(input("question"), a and b become integers, which don't have
# decimals.
a = int(input("enter first number: "))
b = int(input("enter second number: "))

# This function performs different math calculations dependent upon the value of
# c. 
#                       ***When writing functions and conditionals in python,
#                          remember to put a colon (:) at the end of the line**
def doMath(a,b,c):
    if c == 1:
        #add a and b
        return str(a + b)
        
    if c == 2:
        #subtract
        return str(a - b)
        
    if c== 3:
        #multiply
        return str(a * b)
        
    if c == 4:
        #divide
        return str(a / b)
        
    if c == 5:
        #modulo
        return str(a % b)

print("Sum:\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t" + doMath(a,b,5))


