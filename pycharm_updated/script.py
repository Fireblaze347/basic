# selected_word = "snow leopard"
# user_letter = "snow"
# M_selected_word = []

# user_letter_index = [i for i, x in enumerate(selected_word) if x == user_letter]  # A LIST CONTAINING INDEXES (ints)

# for i in range(len(selected_word)):
#     for n in user_letter:
#         if n == selected_word[i]:
#             user_letter_index.append(i)
#             break

# print(user_letter_index)
import random
def generate_list_of_indexes(word):

    index_list = []
    for i in range(int(len(word)/2)):
        index_list.append(random.randint(0,len(word)))

    return index_list

print(generate_list_of_indexes("hello"))