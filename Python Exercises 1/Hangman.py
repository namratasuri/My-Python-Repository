HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

def get_random_word():
     with open(".\Txt Files\sowpods.txt", "r") as wordFile:
         wordList = []
         word = wordFile.readline().strip()
         while word:
             wordList.append(word)
             word = wordFile.readline().strip()
     random_number = int(input("Please enter a number between 1 and %d : " %(len(wordList))))
     print("A random word has been selected - let's begin playing Hangman")
     return wordList [random_number]


def get_user_input(hangman_word):
    guess_word = ['_ ' for x in hangman_word]
    print(''.join(guess_word))
    list_of_guessed_alphabets = []
    incorrect_guess_count = len(HANGMAN)
    while ''.join(guess_word) != hangman_word and incorrect_guess_count > 0:
        user_input = str(input("Please enter an alphabet between a-z: ")).lower()
        if user_input in list_of_guessed_alphabets:
            print("You already guessed this alphabet - please try another alphabet")
        elif user_input in hangman_word:
            foo = [pos for pos, char in enumerate(hangman_word) if char == user_input]
            for x in range (0, len(foo)):
                guess_word[foo[x]] = user_input
            print (''.join(guess_word))
        else:
            print ("Incorrect guess !")
            incorrect_guess_count -=1
            print(HANGMAN[-incorrect_guess_count-1])
            # print("You have %d incorrect guesses left" % incorrect_guess_count)
        list_of_guessed_alphabets.append(user_input)
    if incorrect_guess_count:
        print('Word guessed correctly !!')
    else:
        print('Game Over ! Loser !')



def main():
    hangman_word = get_random_word()
    get_user_input(hangman_word.lower())



if __name__ == '__main__':
    main()