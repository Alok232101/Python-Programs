# def is_palidrom(word):
#     reverse_word  = word[::-1]
#     if word == reverse_word:
#         return True
#     else:
#         return False
    
# def is_palidrom(word):
#     if word == word[::-1]:
#         return True
#     return False

def is_palidrom(word):
    return word == word[::-1]

print(is_palidrom("racecar"))
print(is_palidrom("Alok"))
