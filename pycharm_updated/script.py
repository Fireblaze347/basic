selected_word = "buffoon"
user_letter = "oo"

user_letter_index = [i for i, x in enumerate(selected_word) if x == user_letter]  # A LIST CONTAINING INDEXES (ints)

print(user_letter_index)