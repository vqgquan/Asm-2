# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 18/12/2021
# Last modified date: 18/12/2021

def encode_str(s):
    """
    A function to encode the str into number
    :param s:string
    :return:string
    """
    # Call empty variable to store items later on
    x = ""
    final = ""
    number = []
    # Make a for loop to both translate and reverse the string
    for i in range(len(s)):
        x = x + str(ord(s[i]))[::-1]
    # Add all the newly translated to the number list
    for i in range(len(x)):
        number.append(int(x[i]))
    # Make a for loop to add 1 to even position and if it's 9 then turn it into 0
    for i in range(len(number)):
        if i % 2 == 0 and number[i] != 9:
            number[i] += 1
        elif number[i] == 9:
            number[i] = 0
    # Convert all data in number to string
    string = [str(x) for x in number]
    # Add all string value calculated above to final
    for i in range(len(number)):
        final = final + string[i]
    # Return final
    return final


# Execute the function
print(encode_str("AiQa1n3lKxWFJPj"))
print(encode_str("thFgiR0d4C7TXrY"))
