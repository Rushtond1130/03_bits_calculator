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

# Main routine goes here
statement_generator("hello world", "-")
