# Handling_Errors
# the following code works but cannot handle invalid input
# if the user inputs something other than an integer at first, the program will break due to a ValueError,
# caused by calling int() function on an non-integer input result
#
# SOLUTION:
# used the try-except-else-finally workflow and handled the error
# whenever a user provides a non-integer input, the error message will be displayed: 'Please input integers only.'
# then the user will be asked: 'Do you want to play again? (y/N):'
