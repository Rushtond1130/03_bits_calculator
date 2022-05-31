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


# main routine
instructions() 