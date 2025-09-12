#Learning the rules of variable naming in Python.

name = "Artemis"
lenght = len(name)
print(lenght)

#Also, we can changed the variable names as:

n = "Alvaro"
l = len(n)
print(l)

#But is not recommended, because when someone need to check the code, it will be difficult to understand what it is doing.
# So, we must be more explicit with variables' names.

# Rule 1: make the code readable.

# Rule 2: Name of the variable, has to be one single unit. As in:
username = "Rosario"
# and not "user name", without the underscore sign, between the two words.

# Rule 3: we can use numbers in variables, as an example: for the lenght variable, we could have lenght1, lenght2, etc...but never the number in front of variable, as in 1lenght, 2lenght, etc. This generates a syntax error.

#Rule 4: be careful with typos in the variables names. As in nima, and then nomo.

nima = "Heriberto"
lenght = len(nima)
print(l)

nimo = "Lisa"
lenght = len(nomo)
print(l)

#Expect an error.