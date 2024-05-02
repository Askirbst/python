def check():
    try:  #determine if they are providing what we asked for
        num = int(input("Please enter a number that is divisible by either 3 or 5, and I will tell you which it is divisible by: "))  # Ask for an input and add to integer
    except ValueError:
        print("Come on man, please enter a valid number!  Do you even know what an integer is?") # if not an integer, talk shit.
        return #spit out the num var to be used in next sequence?

    if num % 3 == 0:
        print("foo - This number is divisible by 3")  # Print 'foo' if number is divisible by 3
    if num % 5 == 0:
        print("faa - This number is divisible by 5")  # Print 'faa' if number is divisible by 5
    else:
        print("This number is neither divisble by 3 nor 5!  Did you even read the instructions?") #Otherwise, Print this number is neither divisible by 3 nor 5

# Call the function that was definied back to run it
check()

