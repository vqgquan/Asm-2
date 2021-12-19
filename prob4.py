# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 18/12/2021
# Last modified date: 19/12/2021


def encode_str(s):
    """
    A function to encode the str into number
    :param s:string
    :return:string
    """
    # Call empty variable to store items later on
    encoded_s = ""
    num_list = []
    # Make a for loop to both translate and reverse the string
    for i in s:
        x = str(ord(i))[::-1]
        num_list.append(x)
    # Make a for loop to calculate the next number
    for j in range(0, len(num_list)):
        # Define first_time variable to store num_list at j position
        first_time = num_list[j]
        # Add conditional statement to skip over the first character and return itself then start again at even postion
        if j % 2 != 0:
            # Make a for loop to test each condition and add 1 accordingly
            for k in range(len(first_time)):
                # Define variable which will reset after each loop
                second_time = ""
                y = first_time[k]
                # Conditional statements for how the program will add 1 to "even" position
                if k % 2 == 0 and int(y) != 9:
                    second_time += str(int(y) + 1)
                elif k % 2 == 0 and int(y) == 9:
                    second_time = str(0)
                else:
                    second_time += str(y)
                # Add the newly calculated value back into encoded_s
                encoded_s += second_time
        # Return the value to it to encode_s without changing anything
        else:
            encoded_s += first_time
    # Return encoded_s
    return encoded_s


# Execute the function
# print(encode_str("6o3UiZ"))
# print(encode_str("UPIFS26HfVb30NuKWBC"))
# print(encode_str("k3DAVhUYXd"))
