# Python Challenge - MSP (ENGR4)

#Written by Sean Lynch

#10.12.2021




print("Hang Man Game")

play_game = input("press Enter to start")

# these lines are where I assign to each number of mistakes a specific stage of hangman
mistake0 = "---┐"
mistake1 = "---┐ \n   O \n   "
mistake2 = "---┐ \n   O \n   | "
mistake3 = "---┐ \n   O \n  \| "
mistake4 = "---┐ \n   O \n  \|/ \n    "
mistake5 = "---┐ \n   O \n  \|/ \n   | \n   "
mistake6 = "---┐ \n   O \n  \|/ \n   | \n  /  "
mistake7 = "---┐ \n   O \n  \|/ \n   | \n  / \ "

a = 0    # this variable represents the number of mistakes player 2 makes
b = 0    # this variable represents the digit from the original word:  if the word is rabbit and b = 2, b is 'a'

def mistakes(a):
    if a == 1:
        print(mistake1)
    if a == 2:
        print(mistake2)
    if a == 3:
        print(mistake3)
    if a == 4:
        print(mistake4)
    if a == 5:
        print(mistake5)
    if a == 6:
        print(mistake6)
    if a == 7:
        print(mistake7)


    
    
    


while play_game == "y" or play_game == "":
    
    word = input("Player 1, what's the word? ")
    print("\n" * 50)    #This line "clears" (meaning it just prints a whole bunch of empty lines)
                        #the serial monitor so that player 2 can't see the original word.
    print(mistake0 + "\n" * 2)
    #print(c)
    
    correctGuesses = ""    # correctGuesses is a string that stores the letters from correct guesses
    missedGuesses = ""    # missedGuesses is a string that stores the letters from missed guesses, so player 2 knows what they got wrong before they
                          # make another guess
    
    correctGuess = ""     # correctGuess turns into a boolean that stores whether player 2's guess was in the word or not
    
    blanks = "_" * len(word)  # These two variables had to be created inside the while loop in order for the program to know I had defined 'blanks'.
    seperator = " "
    
    def currentGuesses(b, correctGuesses, blanks):   # this function takes the _ blanks and replaces them with correctly guessed letters
        for correctGuesses in word:
            if correctGuesses == word[b]:
                blanks = blanks[:b] + word[b] + blanks[b + 1:]
        return blanks  


    while True:
        print()
        newGuess = input("Player 2, guess a letter or word: ")
        
        if len(newGuess) != 1: 
            print("Can't guess more than one letter")
            continue
        
        if newGuess in word: 
            correctGuess = True
        if newGuess not in word:
            correctGuess = False
        
        if correctGuess == True:
            
            if newGuess in correctGuesses:
                print("\n" + "Second time you guessed that, it was correct")
            else:
                correctGuesses = correctGuesses + newGuess
            
            b = 0
            
            for guess in word:
                
                guess = newGuess
                val = word[b]
                
                if val == guess: 
                    blanks = currentGuesses(b, correctGuesses, blanks)
                    f = seperator.join(blanks)   # this line puts spaces inbetween the blanks of the word when guessing
                                                 # _ _ _ _ instead of ____ 
                    
                b = b + 1
            print(f + "\n")
            
            
        if correctGuess == False:
            
            a = a + 1
            
            mistakes(a)
            
            print(f + "\n")
            
            if newGuess in missedGuesses:
                print("Second time you guessed that, it was incorrect" + "\n")
            else:
                
                if a == 7:   # this if statement reads if player 2 has ran out of mistakes or not,  the game ends
                    print("GAME OVER" + "\n")
                    print("The word was: " + word)
                    break
                
                missedGuesses = missedGuesses + newGuess + " "
            print("Missed Guesses: " + missedGuesses + "\n")
        if blanks == word:
            print("You Won!")
            break
    
    play_game = input("Do you want to play again? (y/n)" + "\n")
