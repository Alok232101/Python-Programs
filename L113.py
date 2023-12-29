# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# function used with tuples

mixed=(1,2,3,4.0,'five','SIX','IV')

# for loop in tupe
for i in mixed:
    print(i)
# note: we can use while loop too
    
# tuple with one element
num=(1,) #(,)NOTED
word=('ALOK')
print(type(num))
print(type(word))

# tuple without parenthesis
gutar = 'yamaha', 'baton rouge', 'taylor'
print(type(gutar))

# tuple unpacking
guitarists = ('maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitarists1, guitarists2, guitarists3=(guitarists)
print(guitarists1)
print(guitarists2)
print(guitarists3)
print(guitarists)

# list inside tuples
favorites = ('south mangolia', ['Tokyo Ghoul Theme','landescape'])
favorites[1].pop()
favorites[1].append('we made it')
print(favorites)

# min(), max(), sum
num=(1,2,3,4,5,6)
print(min(num))
print(max(num))
print(sum(num))
