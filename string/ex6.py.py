#ex6.py
#using embedded string and texts (format)
#practice by ZED A SHAW

#declaration of values
types_of_people = 10
x = f"there are {types_of_people} types of people ."

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"i siad: {x}")
print(f"i also said: {y} ")

#using format() function
hilarious = False
#curly brackets are written where you want to write the declared data using format.
joke_evaluation  = "isn't that joke so funny ?! {}"
# use '.' for using the format function.
print(joke_evaluation.format(hilarious))

w = "this is left side of..."
e = "a string with a right side."
print(w + e)
#concatenation of two strings
