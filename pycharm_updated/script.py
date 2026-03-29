selected_word = "snow leopard"
user_letter = "snow"
M_selected_word = []

user_letter_index = [i for i, x in enumerate(selected_word) if x == user_letter]  # A LIST CONTAINING INDEXES (ints)

for i in range(len(selected_word)):
    for n in user_letter:
        if n == selected_word[i]:
            user_letter_index.append(i)
            break

print(user_letter_index)