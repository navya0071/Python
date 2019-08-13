formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
#double quotes are important to print here or you can use single quotes
print(formatter.format('one',
'two',
'three',
'four'))
print(formatter.format(True,False,False,True))
#formatter in the next line under format function will print the declared value
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
  "Try Your",
  "Own Text here",
  "Maybe a poem",
  "Or a song about fear"
))
