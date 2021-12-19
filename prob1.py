# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 18/12/2021
# Last modified date: 18/12/2021

# first_piece = ['8g5NLsQQ5pW94W3BCm', '5LT5Ienbf2HQ', '4XnieV', 'Q9vfm7G', '0WPB49yI8', '8dIomgTLnH7cYO',
# 'XKmAduWLA', 'xVAC6ZlfyWbLi0DbIm', '2hDZgBAne67a', 'v28G1rCHO0P', '9TPGwI']
# second_piece = "00100100011"


# Define translate_code function
def message_decode(str_list, bin_list):
    """
    Define a function that will decode a message using the second code to decipher the first code
    :param str_list:string
    :param bin_list:string
    :return:string
    """
    # Define a variable to store the result
    final_message = ""
    # Make a loop that will sort the string list according to the binary list
    for i in range(len(str_list)):
        # Define a variable to store a listed version of element i from the string list
        change = list(str_list[i])
        # Make a conditional statement to decide whether the element i will be sorted ascending or descending order
        if bin_list[i] == "0":
            change.sort(reverse=False)
        else:
            change.sort(reverse=True)
        # Now the element of i from the string list will be joined again by using "change" variable
        str_list[i] = "".join(change)
        # And the last result will be stored through the join function
        final_message = "".join(str_list)
    # Return final result
    return final_message


# Execute the function
# print(message_decode(first_piece, second_piece))
