# checks input is a number more than the given value
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


# finds number of bits for 24 bit colour
def image_bits():

    # user inputs width and height of image
    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    # calculate the number of pixels
    num_pixels = image_width * image_height
    
    # calculate the number of bits (24 * number of pixels)
    num_bits = num_pixels * 24

    # output the answer and workings
    print()
    print("Number of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    print("Number of bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""

    # main routine
    image_bits()

