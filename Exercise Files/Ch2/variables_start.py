# 
# Example file for variables
#

# Declare a variable and initialize it

f = 0

# print(f)

# # re-declaring the variable works
# s = "hello"

# # ERROR: variables of different types cannot be combined
# print(str(f) + ":" + s )


# Global vs. local variables in functions
def myFunction():
    global f
    f = "123"
    print(f)

myFunction()
print(f)

del f # del statement deletes the definition of the variable that previousely declared.
print (f)