\\Программа считает сколько часов в указанном количестве дней
calc_to_sec = 24
name_of_unit ="hours"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days*calc_to_sec} {name_of_unit}"
    
def validate_and_execute():
    if user_input.isdigit():
        
        user_input_num = int(num_of_days_element)
        if user_input_num > 0:
            calc_value = days_to_units(user_input_num)
            print(calc_value)
        elif user_input_num == 0:
            print("you entered a 0? please,can you  entered a valid positive number")
    else:
        print("your input is not a valid number. DON'T RUIN MY PROGRAM")



user_input = ""
while user_input !="exit":
    user_input = input("Hey user, enter the num of days\n")
    for num_of_days_element in user_input.split(","):
        validate_and_execute()
        