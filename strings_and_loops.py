# Python Program 03 - Strings and Loops (ENGR4)

# Written by Sean Lynch

# 9.23.2021

sentence = input("Type in your text, then press Enter: ")

# This line splits the sentence from input into words in an array
words = sentence.split()

# This for loop breaks down each word in the array, printing out each letter in
# a word on a separate line. When it finishes each word, it exits the inside 
# for loop and prints a dash.
for x in words:
    for n in x:
        print(n)
    print("-")
