from q18 import invert_list
from q13 import conc_lists

l1 = ["G", "u", "i"]
list_aux1 = list()
inverted_list = invert_list(l1, list_aux1)

list_aux2 = list()
palindrome = conc_lists(l1, inverted_list, list_aux2)

print(palindrome)
