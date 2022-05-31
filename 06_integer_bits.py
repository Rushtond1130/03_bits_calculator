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


# converts decemal to binary and states how
# many bits are needed to repersent the original integer
def int_bits():

    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer:", 0)

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (lenth and string above)
    num_bits = len(var_binary)

    #output answer and workings
    
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""

# Main routine here