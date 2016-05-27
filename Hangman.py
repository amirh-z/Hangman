#Import "random" package
import random
#-----------------------------------------------------------------------
#Create some words
WORDS = ["hangman", "chairs", "backpack", "bodywash", "clothing",
         "computer", "program", "glasses", "friends", "clock", "shampoo",
         "suitcase" 
        ]
#-----------------------------------------------------------------------
#Create Hangman pictures
HANGMAN = [
#Hangman --> 1
'''
      +-----+
      |     |
            |
            |
            |
            |
            |
    ----------
'''
#Hangman --> 2
,
'''
      +-----+
      |     |
      0     |
            |
            |
            |
            |
    ----------
'''
#Hangman --> 3
,
'''
      +-----+
      |     |
      0     |
      |     |
            |
            |
            |
    ----------
'''
#Hangman --> 4
,
'''
      +-----+
      |     |
      0     |
      |     |
      |     |
            |
            |
    ----------
'''
#Hangman --> 5
,
'''
      +-----+
      |     |
      0     |
      |     |
      |     |
     /      |
            |
    ----------
'''
#Hangman --> 6
,
'''
      +-----+
      |     |
      0     |
     /|     |
      |     |
     /      |
            |
    ----------
'''
#Hangman --> 7
,
'''
      +-----+
      |     |
      0     |
     /|     |
      |     |
     / \    |
            |
    ----------
'''
,
#Hangman --> 8
'''
      +-----+
      |     |
      0     |
     /|\    |
      |     |
     / \    |
            |
    ----------
'''
]
#-----------------------------------------------------------------------
def play_again():
    response = input("Another word? [y,n] ").lower()
    if response == 'y':
        print("\n")
        main() #Call "main" function
    elif response == 'n':
        print("Good luck")
    else:
        play_again()
#-----------------------------------------------------------------------
def main():
    chosen_word = random.choice(WORDS) #Choose random words by computer
    guessed_letters = [] #The letter wich choose by user
    i = 0 #Number of picture
    print(HANGMAN[i]) #Print the first picture of hangman pictures
    word_chars = []
    for char in chosen_word:
        word_chars.append("-")
    attempts = len(HANGMAN) - 1    
    blanks = None
    while attempts != 0 and "-" in word_chars:
        blanks = "".join(word_chars)
        print(" Word : ", blanks)
        player_guess = input("Guess :  ").lower() #Computer get the player guess
        for letter in range(len(chosen_word)):
            if player_guess == chosen_word[letter]:
                word_chars[letter] = player_guess
                if player_guess in guessed_letters:
                    print("you have already guessed '{}'".format(player_guess), "\n")
                else:
                    print("\n")
        if player_guess not in chosen_word:
            if not player_guess.isalpha(): #Check the input is a letter
                print("This is not a letter", "\n")
            elif len(player_guess) > 1: #Check the input is only one letter
                print("This is more than one letter", "\n")
            elif player_guess in guessed_letters:
                print("you have already guessed '{}'".format(player_guess), "\n")
            else:
                attempts -= 1
                i += 1
                print(HANGMAN[i])
        guessed_letters.append(player_guess)            
        if "-" not in word_chars:
            print('Congratulations! "{}" was the word (:'.format(chosen_word))
            play_again()
        if (attempts == 0) and ((attempts == 0) and ("-" in word_chars)):
            print('Sorry, the word was "{}"'.format(chosen_word))
            play_again() #Call "play_again" function
#-----------------------------------------------------------------------
main()
