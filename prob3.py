# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 18/12/2021
# Last modified date: 18/12/2021

def shipment_date(product_amount, start_date):
    """
    Calculate how long will it take for the product be finished
    :param product_amount:integer
    :param start_date:integer
    :return:
    """
    # Define a dictionary to store all necessary information
    dic = {
        "A": {
            "days off": [2, 0],
            "product_a_day": 8,
        },
        "B": {
            "days off": [3, 0],
            "product_a_day": 10,
        },
        "C": {
            "days off": [1, 6, 0],
            "product_a_day": 12,
        },
    }
    # Define some variable to store data for latter usage
    current_day = start_date
    total_product = 0
    total_day = 0
    estimated_day = 0
    # Add conditional statement to decide when the program is going to start and stop running
    while total_product < product_amount:
        # Add conditional statement to decide product make each day
        if current_day == 2:
            product_made_a_day = 22
        elif current_day == 3:
            product_made_a_day = 20
        elif current_day == 1:
            product_made_a_day = 18
        elif current_day == 0:
            product_made_a_day = 0
        elif current_day == 6:
            product_made_a_day = 18
        else:
            product_made_a_day = 30

        # Calculate total product
        total_product += product_made_a_day
        # Calculate total days
        total_day += 1
        # Calculate the current day
        current_day = (current_day + 1) % 7
    # Return total_day
    return total_day


# Execute the function
print(shipment_date(375, 3))
