def interact():
    while True:  # keep looping until user reach break statement
        try:
            user_input = int(input('Please input an integer:'))  # turn the user input into an integer
        except ValueError:
                print("Your input was not valid.")
        else:
            if user_input % 2 == 0:
                print(f"{user_input} is even.")
            else:
                print(f"{user_input} is odd.")  # print out the message '{user_input} is {even/odd}.'
        finally:
            user_input = input('Do you want to play again? (y/N):')
            if user_input != 'y':   # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit
            else:
                continue
interact()