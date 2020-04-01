string = "Hey there. What is your name?!" #splits at "there"
newords = string.split("there") #creates a list of strings called newords which is split at there

print(newords)


#This splits the string into a bunch of strings grouped together in a list. Since this example splits at "there", the first item in the list will be "Hey ", and the second will be ". What is your name?!"
