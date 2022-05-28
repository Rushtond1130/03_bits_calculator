# Checks if user choice is 'interger', 'text' or 'image'
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


# Main routine goes here
keep_going = ""

while keep_going == "":
    data_type = user_choice()
    print("you chose", data_type)

    print()
