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


