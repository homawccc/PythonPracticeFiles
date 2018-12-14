# import ex25  --requires ex25. precede statements
from ex25 import *
sentence = "All good things come to those who wait."
#words = ex25.break_words(sentence)
words = break_words(sentence)
sorted_words = sort_words(words)
print(words)

#print(ex25.sort_words(words))
print(sort_words(words))  #sort_words function only returns, no print statement

print_first_word(words)  #"print" statment is in existing function

print_last_word(words)  #"print" statment is in existing function

print(words, "first and last words removed")
"""first and last were removed with pop(0) and pop(-1)
from p_f_w and f_l_w functions"""

print_first_word(words)
print_last_word(words)

print_first_word(sorted_words)
print_last_word(sorted_words)
print(sorted_words)

sorted_words = print(sort_sentence(sentence))  #sorts original list of words from sentence

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)