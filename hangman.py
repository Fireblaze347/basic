import random
import sys
import os
import re
import time

word_list = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"] #list of words that can be asked
selected_word = random.choice(word_list) #the selected word (chosen randomly)
known_letter_indexes  = [2, 6]
letter_counter = 0
current_word = []
wrong_guessed_words = []
mistakes = 0


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def clear():
    os.system("clear")

clear()

#FYI they are allowed 6 mistakes
for letter in selected_word:
    ###cu
    if letter_counter in known_letter_indexes:
        current_word.append(letter)
        
    else:
        current_word.append("_")
    letter_counter += 1

 

#Game loop
while True:
    print(HANGMANPICS[mistakes])
    if wrong_guessed_words:
        print(f"You have guessed {", ".join(wrong_guessed_words)} wrongly already")
    print()
    print(" ".join(current_word))
    print()
    user_letter = input("Guess a letter... ")
    
    if re.search(r"[a-z]", user_letter):
        #if they found the word early and guess it fully
        if user_letter == selected_word:
            break


        if user_letter in selected_word:
            #Check for multiple entries of a letter! IMPORTANT!

            user_letter_index = [i for i, x in enumerate(selected_word) if x == user_letter] #A LIST CONTAINING INDEXES (ints)

            #TRUE if more than one item
            if len(user_letter_index) > 1:
                #iterate over every extra one found
                for specific_letter in user_letter_index:
                    current_word[specific_letter] = selected_word[specific_letter]
            else:
                #only one so we just take the first(only) one
                #userletterindex[0] returns an int with the index!
                current_word[user_letter_index[0]] = selected_word[user_letter_index[0]]

        else:
            #the user is wrong 
            if user_letter not in wrong_guessed_words:
                wrong_guessed_words.append(user_letter)
            
                print("Letter not present! ")
                print()
                mistakes += 1
        
        if "".join(current_word) == selected_word:
            #win
            break

        if len(wrong_guessed_words) > 6:
            print("You lost!")
            print()
            print(f"The word was: {selected_word}")
            sys.exit()


        clear()
    else:
        #not a letter
        clear()
print("You win!")
