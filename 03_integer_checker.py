# Checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter a number that is more than (or equal to) {}".format(low)
        

        try:

            # Ask the user for a number
            response = int(input(question))

            # Checks if number is more than zero
            if response >= low:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()
            
        except ValueError:
                print(error)

# Main routine goes here

keep_going = ""
while keep_going == "":

    print()
    # Ask user for an integer (must be more than or equal to 0)
    var_integer = num_check("Enter an integer:", 0)
    print()

    # Ask for width & height of an image
    # (must be more than or equal to 0)
    image_width = num_check("Image width? ",1)
    print()

    image_height = num_check ("Image height? ",1)
    