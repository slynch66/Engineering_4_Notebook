# Engineering_4_Notebook
## Table of Contents
* [Python_Dice_Roller](#PythonDiceRoller)
* [Python_Calculator](#Python_Calculator)
* [Python Quadratic Solver](#Python_Quadratic_Solver)
* [Python Strings and Loops](#Python_Strings_and_Loops)
---

## Python_Dice_Roller

Okay so I am giving you a freebie so you have an example of the kind of reflections that I want. I'll start you off with an example for dice_roller.py, then its up to you to start your reflections with the Python calculator and all subsequent assignments. You can delete this section from your personal readme. 

### Assignment Description

The purpose of this assignment was to create a program that can automatically roll dice. The program also took user input to decide whether another dice should be rolled, or if the program should exit. The spicy version added complexity by asking the user to specify the number of sides on the dice and the number of dice to be rolled at a time. The user was then asked whether they wanted to roll again with the same settings, change the settings, or exit the program. 

### Evidence 

Vanilla version:

![Screenshot 2021-09-10 3 15 26 PM](https://user-images.githubusercontent.com/89222808/133513775-a3eafb43-f836-4e4f-8aa6-e28ca584901f.png)

Spicy version:

![Screenshot 2021-09-10 3 18 38 PM](https://user-images.githubusercontent.com/89222808/133513750-727cdb6c-1c27-4c8a-83d4-50ea9136a221.png)

### Code

[Commented code](https://github.com/slynch66/Engineering_4_Notebook/blob/main/README.md#Python_Calculator)

### Reflection

This assignment was relatively simple, but was challenging because I had not coded in Python for several months. I learned that I could import parts of toolboxes without importing the entire thing, but that changes the syntax of how I call the function later. I also learned about using a while loop to control whether a user wants to exit the program. For the spicy version, I needed to use nested loops. Python determines what is inside a loop by the indent level of each line of text, rather than brackets like some other coding styles. That means I need to be really careful with my tabs!


## Python_Calculator

### Assignment Description

For the Python Calculator assignment we needed to write a program that asked the user to input two numbers, and then it would print out the sum, difference, product, qoutient and modulus of the two inputs. The program would do all of the calculations using the same **doMath()** function, 5 different times. 

### Evidence 

![pic-of-code-and-serial-monitor](https://raw.githubusercontent.com/slynch66/Engineering_4_Notebook/main/images/python_program_01.PNG)

### Reflection

I found this assignment pretty challenging because in one of my other classes we're writing in javascript, and I couldn't remember what python was like. I learned how to break down the function into many different conditions. This simplified my overall code so that I didn't have to write out the math inside the print lines. I learned that in python you have to write "return" before your math on the same line in order for the function to return the value from the math. Otherwise, the function will do the math but won't return the answer outside of the function. I also learned that you have to convert numbers to strings in order to print them out along with text. You can do this using the str() command.

## Python Quadratic Solver

### Assignment Description

For the Quadratic Solver assignment we needed to write a program that asks the user for the a, b, and c coefficients of a quadratic equation. We take the new equation it gives us and print out the roots of the quadratic is it has some, and if there are no real roots it will print that out too. We had to take the discriminant in order to find out if the equation has real roots or not. Once it prints out the roots, we have to ask the user to press Enter to run another equation or 'x' then Enter to quit.

### Evidence

![pic-of-code-and-serial-monitor](https://raw.githubusercontent.com/slynch66/Engineering_4_Notebook/main/images/python_program_02.PNG)

### Reflection

One program format that I'll need to remember is the format I use in order to run the program when they press Enter, run it again if they press Enter, and stop the program if they press 'x' then Enter. This is the format I use to do that:
```python
retry = input("press Enter to start")

while retry == "":
    Program Code
    retry = input("press Enter to start or 'x' then Enter to quit: ")
```

## Python Strings and Loops

### Assignment Description

For this assignment we had to write a program that asks the user to input a sentence. The program then takes the sentence and prints it back out one letter at a time, with dashes in between each word.

### Evidence

![pic-of-code-and-serial-monitor](https://raw.githubusercontent.com/slynch66/Engineering_4_Notebook/main/images/strings_and_loops.PNG)

### Reflection

When this code runs, this nested for loop prints out each letter of a word on separate lines. When it finishes the word, it exits the nested for loop and prints a dash. As long as there are more words to run through from the array, the outer for loop will continue to run.
```python
words = sentence.split()

for x in words:
    for n in x:
        print(n)
    print("-")
```

### Sources 
https://www.w3schools.com/python/python_for_loops.asp
