# insert method
# join (concatenate) two list
# extent method
# difference between append and extend

fruits1=['apple','mango']
fruits1.insert(1,'grapes')
print(fruits1)

print("\n")

fruits2=['orange','papaya']
fruits2.insert(1,'grapes')
fruits=fruits1+fruits2
print(fruits)
print("\n")

fruits1.extend(fruits2)
print(fruits1)

fruits1.append(fruits2)
print(fruits1)

