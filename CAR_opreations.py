"""
Document:   Car showroom info management system
Created on: 23rd of September 2021, 6:30:12 PM
Last updated : 30th of September 2021, 12 PM
"""


from car_info_manage_methods import ManageCarInfo
from carpro_exception import InputInvalid, YearSizeInvalid

car_op = ManageCarInfo()
print("Welcome")
# Method to select options
while True:
    print("#1-Add cars to the list")
    print("#2-Check the availability of cars")
    print("#3-Check all available car from database")
    print("#4-Delete purchased items from the lists")
    print("#5-Quit\n")
    user_task = input("Please choose one feature from above:")
    # Method to enter Car name, Car manufacture year, Car color, Car price
    if user_task == "1":
        while True:
            car_name = input("Enter the name of car: ")
            while True:
                verify_name = input("Verify the name of car:{} is correct or not\nans(y/n)-->".format(car_name))
                if verify_name == "Y" or verify_name == "y" or verify_name == "N" or verify_name == "n":
                    break
                else:
                    print("-----------Please Enter a valid response--------------------------------------------")
            if verify_name == "Y" or verify_name == "y":
                print("Car name added")
            else:
                continue
            while True:
                car_model_no = input("Please enter the model number of car: ")
                while True:
                    verify_no = input("Verify the model number of car: '{}' is correct or not\nans(y/n)-->".format(car_model_no))
                    if verify_no == "Y" or verify_no == "y" or verify_no == "N" or verify_no == "n":
                        break
                    else:
                        print("-------------------------Please Enter a valid response---------------------------")
                if verify_no == "Y" or verify_no == "y":
                    break
                else:
                    continue
            while True:
                car_year = input("Enter Manufactured year of car: ")
                # Checking user input is correct or not
                try:
                    if not car_year.isnumeric():
                        raise InputInvalid
                    if len(car_year) < 4 or len(car_year) > 4:
                        raise YearSizeInvalid
                    if int(car_year) > 2021:
                        raise InputInvalid
                except InputInvalid:
                    print("Please enter the valid  year")
                    continue
                except YearSizeInvalid:
                    print("Please enter a valid year ")
                    continue
                while True:
                    verify_year = input("Please verify the year: '{}' is correct or not\nans(y/n)-->".format(car_year))
                    if verify_year == "Y" or verify_year == "y" or verify_year == "N" or verify_year == "n":
                        break
                    else:
                        print("-----------------Please Enter a valid response----------------------------")
                if verify_year == "Y" or verify_year == "y":
                    print("Car year added")
                    break
                else:
                    continue
            while True:
                car_color = input("Enter color of car: ")
                # Checking user input is correct or not
                try:
                    if not car_color.isalpha():
                        raise InputInvalid
                except InputInvalid:
                    print("Please enter the valid Word input not numbers")
                    continue
                while True:
                    verify_color = input(
                        "Please verify the color: '{}' is correct or not\nans(y/n)-->".format(car_color))
                    if verify_color == "Y" or verify_color == "y" or verify_color == "N" or verify_color == "n":
                        break
                    else:
                        print("----------------------Please Enter a valid response-----------------------------")
                if verify_color == "Y" or verify_color == "y":
                    print("Car color added")
                    break
                else:
                    continue
            while True:
                car_price = input("Enter the price of car: ")
                while True:
                    verify_price = input("Please verify the price:'{}' is correct or not\nans(y/n)-->".format(car_price))
                    if verify_price == "Y" or verify_price == "y" or verify_price == "N" or verify_price == "n":
                        break
                    else:
                        print("-------------------Please Enter a valid response---------------------------------")
                if verify_price == "Y" or verify_price == "y":
                    break
                else:
                    continue
            car_op.add_car_items(car_name, car_model_no, car_year, car_color, car_price)
            user_task1 = input("Do you want to add more cars?\nans(y/n)")
            # Checking user input is correct or not
            while True:
                if user_task1 == "Y" or user_task1 == "y" or user_task1 == "N" or user_task1 == "n":
                    break
                else:
                    print("---------------Please Enter a valid response-------------------------")
            if user_task1 == "Y" or user_task1 == "y":
                continue
            else:
                break

            # method to repeat the option add cars to car inventory on user demand

    # Method to print available cars
    elif user_task == "2":
        while True:
            find_car_data = input("Enter name of car to search in database: ")
            car_op.check_availability(find_car_data)
            # Method to repeat find car option on user demand
            while True:
                user_task2 = input("Do you want to search for other items\nAns(y/n)-->")
                if user_task2 == "Y" or user_task2 == "y" or user_task2 == "N" or user_task2 == "n":
                    break
                else:
                    print("----------------Please Enter a valid response----------------")
            if user_task2 == "Y" or user_task2 == "y":
                print("Ok")
                continue
            else:
                break
    # Method to display all the available car
    elif user_task == "3":
        car_op.check_all_available_cars()
    elif user_task == "4":
        while True:
            del_str1 = input("Enter purchased car model no: ")
            car_op.del_car_items(del_str1)
            while True:
                user_task3 = input("Do you want to delete more purchased items?\nans(y/n)-->")
                if user_task3 == "Y" or user_task3 == "y" or user_task3 == "N" or user_task3 == "n":
                    break
                else:
                    print("-----------Please Enter a valid response-----------------")
            if user_task3 == "Y" or user_task3 == "y":
                continue
            else:
                break
    elif user_task == "5":
        print("\n\n-----------------------Bye-----------------------------------")
        break
    else:
        print("-------Enter a valid option------")
        continue
