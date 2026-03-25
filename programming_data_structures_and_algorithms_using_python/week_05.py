# --- Exception Handling ---
# Errors can be anticipated or unexpected. 
# Exception - predictable errors
# Exception handling - contingency plan for exception. If something goes wrong, provide 'corrective action'
# eg., SyntaxError, NameError, ZeroDivisionError, ...

# Terminology
#   * Raise an error
#   * Handle an exception
#   * Unhandled exception aborts excecution


# Postive use of exceptions -> Traditional approach
scores = {'Dhawan':[3, 22], 'Kohli':[200, 3]}
if b in scores.keys():
    # If player b already exists → it adds (append) the new score s to their list.
    scores[b].append(s)
else:
    # If player b does NOT exist → it creates a new entry with [s].
    scores[b] = [s]

# Postive use of exceptions -> Using exceptions
try:
    # # If player b already exists → it adds (append) the new score s to their list.
    scores[b].append(s)
except KeyError:
    # If player b does NOT exist → it creates a new entry with [s].
    scores[b] = [s]



# --- Standard input and standard output ---
# Input is always a string, convert as required
input_data = input()
input_data = input('Enter here: ')

while True:
    try:
        userdata = input("Enter a number: ")
        usernum = int(userdata)
    # if error then it will return True after exception
    except ValueError:
        print("Not a number. Try again")
    # if number is entered then after try else will be excecuted
    else:
        break 

# printing to screen
print(x)
print(x, y)
print("Not a number")
print(x,"Not a number", sep=" ")  # separate 2 of them with space
print(f"{x} not a number")

print("continue on the", end=" ")  # add space, no new line
print("same line", end=".\n")  # add full stop, new line
print("next line.")
# output
# continue on the same line
# next line