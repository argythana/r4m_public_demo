"""
BIS UOA course
author: Argyriou Thanasis
Lecture 1, part E, Introduction to syntax, style, PEMDAS.
"""

# load python modules with import.
# We will learn about modules and imports soon, but not today.
import sys
import os

# Command to show python version within a script.
print(sys.version)
print()  # Print an empty line.


# Command to show working directory within a script.
print(os.getcwd())
print()

"""Introduction to python.
Valid syntax and invalid syntax.
Use the **# sign** for comments in python. The interpeter ingores them.
Used to leave hints.
"""

"""Docstrings are a text which is enclosed in triple quotes.
Docstrings are used for documentation purposes. Not for comments."""

# This # sign denotes a comment in python code. It is not executed.
# A line that starts with # is "ignored" by python interpreter.

"""Variables are defined by a pair of a ***name*** and a ***value***.
The **equal sign** assigns a value to a variable name
Variables are objects with names, not exactly variables.
Always define variables before using them, similar to math problems.
"""

x = 3
y = 4
z = x + y

print(x, y, z)

# Whitespaces in the beggining matter in python.
# The line below has a whitespace in the beginning.
# It will raise an "Indentation error" if you uncomment it.
# And it will interrupt the execution of the python script.
#  z = 9


"""Case-sensitive syntax."""
"""In python "Giannis and Giannakis" is not at all the same thing."""
A = 4
a = 5


"""
When not in interactive mode, we get no output without print.
Output is different in interactive mode than in non-interactive mode.
"""
A  # This returns no output when using IDLE.
a  # This returns no output when using IDLE.

# To show output to user use print().
print(A)
print(a)
print()


"""Starting "names" with numbers is NOT allowed."""
a1 = 2  # This is allowed.
print(a1)

# 1a as a variable name is NOT allowed.
# Uncomment it to raise a "syntax error".
# 1a = 4


print("Hello class!")
print()

# print(hello class)  # Invalid syntax because of missing quotes.

# print(helloclass)  # print value of variable with name helloclass
# => NameError: No variable has been defined with that name.
# Python says: "I don't know who is helloclass".


"""Python style guide. Readability counts!
[Python PEP8 style guide](https://www.python.org/dev/peps/pep-0008/)
[Documentation for whitespaces](https://www.python.org/dev/peps/pep-0008/)
[Documentation for Naming Conventions](https://www.python.org/dev/peps/pep-0008/)
[Check a helper for code styling errors:](http://pep8online.com/)

Readability and usability before style.
Use PEP8 style.
One of the reasons for python popularity.
SOS: debugging (finding errors) takes more time than coding!
Use white spaces when needed to increase readability and debugging.
Use descriptive names. Another reason for python popularity.
"""
print("For this course, all file names, variable names, directory names etc, should be:\n\
only in English,\n\
without blank spaces,\n\
no uppercase letters,\n\
=> use 'snake_case_format' .")

"""The operations below will not be returned as output.
because I did not use print.
Please copy and paste them in the interpreter to practice."""
2*a+4*3+A/4*5  # How long does it take to understand what this expression evaluates to?

2*a + 4*3 + (A/4)*5  # Much better, right?


# Optimal style depends on complexity, experience.

x = 1
2 * x + 4 * 3  # Not wrong, not recommended.

(2 * x) + (4 * 3)  # Not wrong, not recommended.

(2*x) + (4*3)  # Ok, but maybe unnecessary parentheses.


# Whitespace around operators with lowest priority in operations.
2*x + 4*3  # Optimal for simple expressions.

(2+x) * (4+3)  # Parentheses and spaces because of operators priority.


"""Order of execution and order of *operations*:
Line by line execution.
Left to right execution, also when equal order of operations.
Names and values are stored in memory.
PEMDAS for math and for python:
(Parentheses, Exponents, Multiplication, Division, Addition, Subtraction).
Always use Parentheses in case of possible ambiguity.
"""

print()
print("Always use Parentheses to diminish ambiguity.")
print(20/5/4)  # Same as print((20/5)/4)
print(20/(5/4))  # Use parentheses because order from left to right MATTERS!
print()

"""Please read the Zen pf python and think about it."""
# The Zen of Python.
import this
