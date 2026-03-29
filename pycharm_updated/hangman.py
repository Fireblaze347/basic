import sys, os, re, random

def clear():
    os.system("cls")

def find_topic_choice():
    return input(" [1] Animals\n [2] Countries\n [3] Food \n [4] Elements\n")


clear()

topic_choice = find_topic_choice()

match topic_choice:
    case "1":
        pass
        

selected_word = "united states of america"  # the selected word (chosen randomly)
known_letter_indexes = [2, 6]
letter_counter = 0
current_word = []
wrong_guessed_words = []
mistakes = 0

hangman_pictures = ['''
   +------+
   |      |
	  |
	  |
	  |
	  |
	  |''', '''
   +------+
   |      |
   O	  |
	  |
	  |
	  |
	  |
''', '''
   +------+
   |      |
   O	  |
   |	  |
   |	  |
	  |
	  |
''', '''
   +------+
   |      |
   O	  |
  /|	  |
   |	  |
	  |
	  |
''', '''
   +------+
   |      |
   O	  |
  /|\	  |
   |	  |
	  |

''', '''
   +------+
   |      |
   O	  |
  /|\	  |
   |	  |
  /	  |
	  |
''', '''
   +------+
   |      |
   O	  |
  /|\	  |
   |	  |
  / \	  |
	  |''']


clear()

# FYI they are allowed 6 mistakes
for letter in selected_word:
    ###cu
    if letter_counter in known_letter_indexes or letter == " ":
        current_word.append(letter)
    
    else:
        current_word.append("_")
    letter_counter += 1

# Game loop
while True:
    print(hangman_pictures[mistakes])
    if wrong_guessed_words:
        print(f"You have guessed {", ".join(wrong_guessed_words)} wrongly already")
    print()
    print(" ".join(current_word))
    print()
    
    user_letter = input("Guess a letter... ")

    if re.search(r"[a-z]", user_letter):
        # if they found the word early and guess it fully
        if user_letter == selected_word:
            break

        if user_letter in selected_word:
            # Check for multiple entries of a letter! IMPORTANT!

            user_letter_index = [i for i, x in enumerate(selected_word) if x == user_letter]  # A LIST CONTAINING INDEXES (ints)


            # TRUE if more than one item
            if len(user_letter_index) > 1:
                # iterate over every extra one found
                for specific_letter in user_letter_index:
                    current_word[specific_letter] = selected_word[specific_letter]
            elif not len(user_letter_index) == 0:            
                # only one so we just take the first(only) one
                # userletterindex[0] returns an int with the index!
                current_word[user_letter_index[0]] = selected_word[user_letter_index[0]]

        elif user_letter not in wrong_guessed_words:
            # the user is wrong
            wrong_guessed_words.append(user_letter)

            print("Letter not present! ")
            print()
            mistakes += 1

        if "".join(current_word) == selected_word:
            # win
            break

        if len(wrong_guessed_words) > 6:
            print("You lost!")
            print()
            print(f"The word was: {selected_word}")
            sys.exit()

        clear()
    else:
        # not a letter
        clear()
        
clear()
print(hangman_pictures[mistakes])
if wrong_guessed_words:
    print(f"You have guessed {", ".join(wrong_guessed_words)} wrongly already")
print()
print(" ".join(current_word))
print()
print("You win!\n")
