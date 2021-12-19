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
    encoded_s = ""
    number = []

    num_list = []
    # Make a for loop to both translate and reverse the string
    for i in s:
        x = str(ord(i))[::-1]
        num_list.append(x)
    # print(num_list)
    for j in range(0,len(num_list)):
        first_time = num_list[j]
        if j % 2 != 0:
            for k in range(len(first_time)):
                second_time = ""
                y = first_time[k]
                if k % 2 == 0 and int(y) != 9:
                    second_time += str(int(y)+1)
                elif k % 2 == 0 and int(y) == 9:
                    second_time = str(0)
                else:
                    second_time += str(y)
                encoded_s += second_time
        else:
            first_time = num_list[j]
            encoded_s += first_time

    return encoded_s


# Execute the function
# print(encode_str("6o3UiZ"))
# print(encode_str("UPIFS26HfVb30NuKWBC"))
print(encode_str("k3DAVhUYXd"))
