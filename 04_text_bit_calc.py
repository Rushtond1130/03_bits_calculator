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
    print("\'{}\' has {} characters.".format(var_text))
    print("number of bits is {} x 8.".format(var_lenth))
    print("We need {} bits to represent {}".format(num_bits, var_text))

    return ""

    # main routine
    text_bits()