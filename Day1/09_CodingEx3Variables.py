#We have two variables glass1 and glass2.
#glass1 contains milk and glass2 contains juice.
# Write 3 lines of code to switch the contents of the variables.
# You are not allowed to type the words "milk" or "juice".
# You are only allowed to use variables to solve this exercises.

glass1 = "milk"
glass2 = "juice"

a = "glass1"
b = "glass2"

vase1 = "b"
vase2 = "a"

# Even when executing the code above this comment and worked, it's not a correct solution of what the exercise is asking for. I couldn't think of just three lines of code, and I work with 4 lines of code. But I'm wrong.

# The exercise brings another glass, a temporary glass. Just one. When I was trying to solve this exercise, I couldn't think about it as a temporary glass. That's why I have used another two.

# I use this two lines of code of print() function to create two lines of space.
print()
print()

# If I follow the logic of the answer to the coach Angela, it will be:

# I was counting the next two lines as part of the 3 lines, which now I noticed I was wrong.
glass1 = "milk"
glass2 = "juice"

# that two lines of code doesn't count as part of the expected 3 lines of code.

# It's from here that the three lines are expected to count.
temp = glass1
glass1 = glass2
glass2 = glass1

# What did happen above is to create a temporary variable to store the contents of just one of the glasses, glass1 or glass2.

# temp = glass1 (or temp = glass2)

# then, by storing the contents of glass1 in the temp variable.

# We can now use the glass1 variable to store the contents of glass2 (because the glass1 is now empty.)

# glass1 = glass2

# Finally, we can put the contents in the temp variable into glass2.

# glass2 = temp

# and that was the answer.


