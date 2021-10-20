"""
Document:   Car showroom info management system
Created on: 23rd of September 2021, 6:30:12 PM
Last updated : 30th of September 2021, 12 PM
"""


# Creating a class ManageCarInfo
class ManageCarInfo:
    # Instance CarInfo with Null Value
    CarInfo = {}

    # Method to add car info
    def add_car_items(self, car_name, car_model_no,  car_year, car_color, car_price):
        self.CarInfo[car_name] = [car_year, car_color, car_price]
        car_name1 = car_name.split(" ")
        car_name2 = [t.upper() for t in car_name1]
        car_name3 = " ".join(car_name2)
        car_check1 = car_name3.split(" ")
        price_split1 = car_price.split(" ")
        new_price_split1 = "-".join(price_split1)
        new_car_name_data_items = "-".join(car_check1)
        car_details_items = new_car_name_data_items + " " + car_model_no + " " + car_year + " " + car_color + " " + new_price_split1
        # Method to save car details in Cardata.txt file
        with open("Cardata.txt", "a+") as my_file:
            my_file.write(car_details_items)
            my_file.write("\n")
        # with open("Cardata,txt", "r") as my_file:
        #     data = my_file.read()
        #     print(data)

    # Method to check items are available or not
    def check_availability(self, find_car_data):
        search_key_check_available1 = [x.upper() for x in find_car_data]
        search_key_check_available2 = "".join(search_key_check_available1)
        search_key_check_available3 = search_key_check_available2.split(" ")
        search_key_check_available4 = "-".join(search_key_check_available3)
        with open("Cardata.txt", "r") as myfile:
            Car_data_in = myfile.readlines()
        Not_found = 0
        found_data = 0
        for car_check_list in Car_data_in:
            car_check_list2 = car_check_list.split(" ")
            if search_key_check_available4[0:4] == car_check_list2[0][0:4]:
                last_value = len(car_check_list2[4])
                print("Car Name: ", car_check_list2[0])
                print("Car Model no : ", car_check_list2[1])
                print("Car Year: ", car_check_list2[2])
                print("Car color: ", car_check_list2[3])
                print("Car price: ", car_check_list2[4][0:last_value])
                found_data += 1
            else:
                Not_found += 1
        if Not_found == len(Car_data_in):
            print("Not available")
        else:
            if found_data > 1:
                print(f"There are {found_data} cars of {find_car_data}")
            else:
                print(f"There is {found_data} car of {find_car_data}")

    # Method to check all available cars
    def check_all_available_cars(self):
        with open("Cardata.txt", "r") as my_file:
            All_data = my_file.readlines()
        total_car = 0
        for datas in All_data:
            total_car += 1
            data2 = datas.split(" ")
            last_value = len(data2[3])
            print("Car Name: ", data2[0])
            print("Car Year: ", data2[1])
            print("Car color: ", data2[2])
            print("Car price: ", data2[3][0:last_value])
            print("\n")
        else:
            if total_car > 1:
                print("There are total {} cars available in stock\n".format(total_car))
                print("\n")
            else:
                print("Only {} cars available in stock\n".format(total_car))
                print("\n")

    # Method to delete purchased items from list
    def del_car_items(self, del_model_no):
        with open("Cardata.txt", "r") as my_file:
            file_data = my_file.readlines()
            r = 0
            new_data_list = []
            for i in file_data:
                mat_data = file_data[r].split(" ")
                if del_model_no != mat_data[1]:
                    new_data_list.append(i)
                r += 1
            if len(new_data_list) != len(file_data):
                with open("Cardata.txt", "w") as my_file2:
                    my_file2.truncate(0)
                with open("Cardata.txt", "w+") as my_file3:
                    for i in new_data_list:
                        my_file3.write(i)
                print("Item deleted")
            elif len(file_data) == len(new_data_list):
                print("Model not found")
