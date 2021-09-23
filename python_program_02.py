# Python Program 02 - Quadratic Solver (ENGR4)

#Written by Sean Lynch

#9.21.2021
from math import sqrt # this will allow me to use the 
print("Quadratic Solver")

retry = input("press Enter to start")


# These two lines ask the user whatever is inside the quotation markes and then
# takes their response and makes that the a or b variable. Because you have a/b
# equals to int(input("question"), a and b become integers, which don't have
# decimals.
a = int(input("Enter the 'a' coefficient: "))
b = int(input("Enter the 'b' coefficient: "))
c = int(input("Enter the 'c' coefficient: "))

# The while loop makes the "Press Enter to start" work and it also makes
# the line below work also:
#       retry = input("press Enter to start or 'x' then Enter to quit: ")

while retry == "":
    print("Enter the coefficients for ax^2 + bx + c = 0")

    def quadSolver(a,b,c):
            
# [The discriminant variable] takes the discriminant of the quadratic equation.
# You can't use the ^ symbol to give something an exponent, you have to multiply
# it by itself : b*b.
        discriminant = b*b - 4 * a * c
        if discriminant < 0:
            roots = ""
            return roots
        else: 
            x = sqrt(b*b - 4*a*c)
            root1 = (-b + x)/(2*a)
            root2 = (-b - x)/(2*a)
            roots = [root1, root2]
            return roots
    roots = quadSolver(a,b,c)
    if roots == "":
        print("There are no real roots.")
    else: 
        print("Root #1: ")
        print(roots[0])
        print("Root #2: ")
        print(roots[1])
    retry = input("press Enter to start or 'x' then Enter to quit: ")
