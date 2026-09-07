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