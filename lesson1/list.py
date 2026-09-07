 squares = [1, 4, 9, 16, 25]
 squares
# [1, 4, 9, 16, 25]
squares[0] # indexing returns the item
# 1
squares[-1]
# 25
#Lists also support operations like concatenation:
squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125] # something's wrong here
4 ** 3
 # the cube of 4 is 64, not 65!
64
cubes[3] = 64 
# replace the wrong valuecubes
[1, 8, 27, 64, 125]
cubes.append(216) # add the cube of 6cubes.append(7 ** 3) # and the cube of 7
cubes
#[1, 8, 27, 64, 125, 216, 343]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
#['a', 'b', 'c', 'd', 'e', 'f', 'g']
 # replace some values
letters[2:5] = ['C', 'D', 'E']
 letters
#['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
 letters
#['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters

#[]
# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
len(letters)
#4
