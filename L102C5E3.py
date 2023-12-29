def reverse_element(l):
    element = []
    for i in l:
        element.append(i[::-1])
    return element

word = ['abc', 'xyz', 'tuv']
print(reverse_element(word))
