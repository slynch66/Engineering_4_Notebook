# Engineering_4_Notebook
## Table of Contents
* [Python_Dice_Roller](#Python_Dice_Roller)
* [Python_Calculator](#Python_Calculator)
* [Python Quadratic Solver](#Python_Quadratic_Solver)
* [Python Strings and Loops](#Python_Strings_and_Loops)
* [Python Challenge - MSP](#Python_Challenge_MSP)
* [Onshape Skateboard](#Onshape_Skateboard)
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

## Python_Quadratic_Solver

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

## Python_Strings_and_Loops

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

https://itsourcecode.com/free-projects/python-projects/hangman-game-in-python-with-source-code/#

## Python_Challenge_MSP

### Assignment Description

For this assignment we had to write a hangman game program. The 'MSP' stands for Man-Shaped-Pinata. The program first asks player 1 for the word, and then player 2 has to guess the word by entering different letters, just like the game hangman. The only difference is you can't guess the whole word at one time (unless you do some spicy stuff).

### Evidence

![pic-of-code-and-serial-monitor](https://raw.githubusercontent.com/slynch66/Engineering_4_Notebook/main/images/msp-challenge-evidence.png)

### Reflection

```python
    def currentGuesses(b, correctGuesses, blanks):   # this function takes the _ blanks and replaces them with correctly guessed letters
        for correctGuesses in word:
            if correctGuesses == word[b]:
                blanks = blanks[:b] + word[b] + blanks[b + 1:]
        return blanks  
```
This was the function that took the blanks displayed to player 2 and changed the blanks to letters each time player 2 would correctly guess a letter from the word. The most important line of code in this function was the line "blanks = ". The three parts that blanks are being set to: 
                    
                    1. The first part ( blanks[:b] ) keeps all of the letters of the word before the correctly guessed letter as blanks. 
                    2. The second part ( word[b] ) replaces the correct blank with the correctly guessed letter.
                    3. The third part ( blanks[b + 1:] ) keeps all of the letters of the word after the correctly guessed letter as blanks. 

## Onshape_Skateboard

### Assignment Description

For this assignment we had to follow the directions in an onshape document to build a skateboard complete with the deck, trucks, wheels and bearings.

### Evidence

![skateboard-evidence](https://raw.githubusercontent.com/slynch66/Engineering_4_Notebook/main/images/skateboard-evidence.PNG)

### Reflection

    - Designing the Deck 
The mirror sketch tool is an excellent time saver that is used for making sketches that are symmetric. All you need to do is draw the shape that you want mirrored, and put in a contruction line as the axis of symmetry. Whatever the distance between what you want mirrored and the axis of symmetry, remember that the distance between the two mirrored sketch entities will be double that.
![mirror-tool-gif](https://www.onshape.com/academic/intro-to-cad/lesson-2-1-5-designing-a-skateboard/assets/614c8660cb9c8285c50d77f0itc_2.1_bo.gif) 

    - Designing the Trucks
When making a new extrude, you can choose to 'Add' the extrude to an existing part or make the new extrude its own 'New' part.
![new/add-extrude](https://raw.githubusercontent.com/slynch66/Engineering_4_Notebook/main/images/designing-the-trucks-reflection.PNG)
When you select 'Add', there is a box at the bottom of the extrude menu that says "merge scope". The merge scope is where you put the existing part that you want to add this extrude to. In order to select another part as the merge scope, the new extrude must be touching that part.

    - Wheels and Bearings


    - Putting it all Together
The revolve mate in assembly studios allows the objects to spin in relation to each other. This is especially helpful for wheels, bearings, or axles. Here is where you find the revolve mate in the menu:
![revolute-mate](https://raw.githubusercontent.com/slynch66/Engineering_4_Notebook/main/images/revolute-mate.PNG)
If you can't find the mate in the menu, you can always search for it on the top right.
