# Checks if user choice is 'interger', 'text' or 'image'
def user_choice():

    valid= False
    while not valid:
        # Ask user for choice and change response to lowecase
        response = input("File type (interger / text / image): ").lower()

        # If "t" or "text" is chosen, return "text"
        if response == "text" or response == "t":
            return "text"

        else:
            # If response not valid, output error
            print("please chose a valid fole type!")
            print()

# Main routine goes here
data_type = user_choice()
print("You chose", data_type)

print()