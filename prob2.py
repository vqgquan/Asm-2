# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 18/12/2021
# Last modified date: 19/12/2021


# dic = {"U": {"luxury": 14, "standard": 37},
# "K": {"luxury": 44, "standard": 5},
# "W": {"luxury": 2, "standard": 5},
# "T": {"luxury": 13, "standard": 31},
# "Q": {"luxury": 25, "standard": 18},
# "O": {"luxury": 36, "standard": 21}
# }


def total_sale(sale_dict):
    """
    A function to calculate total profit of a company, make dictionary to store all sales information, and find the
    best salesperson
    :param sale_dict: dictionary
    :return: integer, dictionary, string
    """
    # Define an empty dictionary,best_salesperson variable and total profit of 0
    profit_dict = {}
    dict_comm = {}
    total_profit = 0
    best_salesperson = ""
    # Make a loop that will calculate all the information needed
    for i in sale_dict.keys():
        # Calculate the profit of each type of tour
        profit_of_standard_tour = sale_dict[i]["standard"] * 200
        profit_of_luxury_tour = sale_dict[i]["luxury"] * 1000
        # Calculate the sum of individuals earnings
        individuals_earning = profit_of_luxury_tour + profit_of_standard_tour
        # Calculate the company's total profit
        total_profit += individuals_earning
        # Add individuals earning back to profit_dict
        profit_dict.update({i: individuals_earning})

        # Calculate the commission of each type of tour for each employee
        standard_comm = profit_of_standard_tour * 0.1
        luxury_comm = profit_of_luxury_tour * 0.2
        # Calculate the sum of both commission
        total_comm = standard_comm + luxury_comm
        # Add information back into the empty list defined above
        dict_comm.update({i: total_comm})

        # Find out the best salesperson by using the max function
        best_salesperson = max(profit_dict, key=profit_dict.get)

    # Return necessary value
    return total_profit, dict_comm, best_salesperson

# Execute the function
# print(total_sale(dic))
