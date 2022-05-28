# Functions go here

# Puts a series of symbols at the satrt and end of the text
def statement_generator(text, decoration):

    # Make string of five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

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

# Main routine goes here

# Title
statement_generator("Bit Calculator For Integers, Text & Images", "-")

# Show instructions for user if user has not used program before

# Loop to allow more than one calculation in a session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # For integers, ask for integer
    if data_type =="integer":
        var_integer = num_check("Enter an integer: ",0)

    # For images, ask for width and height
    # (must be an integer more than / equal to 1)
    elif data_type == "image":
        image_width = num_check("Image width?",1)
        print()
        image_height = num_check("Image height?",1)

    # For text, ask for a string
    else:
        var_text = input("Enter some text:")