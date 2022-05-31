# Functions go here

# Puts a series of symbols at the start and end of the text
def statement_generator(text, decoration):

    # Make string of five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# displays instructions or information
def instructions():

    statement_generator("Instructions  /  Information", "=")
    print()
    print("Please choose a data type (Image / Text / Integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, by pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""
    instructions()

# Checks user choice is "integer" "text" or "image"
def user_choice():

    # Lists of valid response
    text_ok = ["text", "t", "txt"]
    integer_ok =["integer", "int", "#", "number", "num"]
    image_ok = ["image", "img","pix","picture", "pic", "p"]

    valid= False
    while not valid:

        # Ask user for choice and change response to lowecase
        response = input("File type (interger / text / image): ").lower()
        
        # checks if response is valid and returns text, integer or image

        if response in text_ok:
            return "text"
            
        elif response in integer_ok:
            return "integer"
        
        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image  ")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # If response not valid, output error
            print ("please chose a valid file type!")
            print()        

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

# calculates the num of bits for text (num of characters x 8)
def text_bits():


    print()
    # ask the user for a string
    var_text = input("Enter some text: ")

    # calculate the num of bits (lenth of string * 8)
    var_lenth =len(var_text)
    num_bits = 8 * var_lenth


    # output answer with workings
    print()
    print("\'{}\' has {} characters.".format(var_text, var_lenth))
    print("number of bits is {} x 8.".format(var_lenth))
    print("We need {} bits to represent {}".format(num_bits, var_text))

    return ""

    # main routine
    text_bits()

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
    print("Number of bits is {}".format(num_bits))
    print()

    return ""


# Main routine 
# Title
statement_generator("Bit Calculator For Integers, Text & Images", "-")

# Show instructions for user if user has not used program before
first_time = input("Press <enter> to see instructions or any key to continue ")

if first_time == "":
    instructions()

# Loop to allow more than one calculation in a session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # For integers, ask for integer
    if data_type =="integer":
       int_bits()

    # For images, ask for width and height
    # (must be an integer more than / equal to 1)
    elif data_type == "image":
        image_bits()

    # For text, ask for a string
    else:
        text_bits()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")