"""
Intermediate Exercises Workshop 5

1) Get 5 numbers from user and create list within inputs
2) Username Security Checker

"""

# Task 1


def main():
    finalised_list = get_values()
    print("The first number is", finalised_list[0])
    print("The last number is", finalised_list[-1])
    print("The smallest number is", min(finalised_list))
    print("The largest number is", max(finalised_list))
    print("The average of the numbers is", (sum(finalised_list)/len(finalised_list)))


def get_values():
    list_items = []
    while len(list_items) < 5:
        add_to_list = int(input("Number: "))
        list_items.append(add_to_list)
    return list_items
main()


# Task 2


# def main():
#     usernames = ["jimbo", "giltson98", "derekf", "Whatsup", "Nicoleye", "swei45", "BaseInterpreterInterface",
#                  "BaseSTDIn", "Command", "ExecState", "InteractiveConsole", "InterpreterInterface", "StartServer", "bob"
#                  ]
#     user_username = input("Username: ")
#     if user_username in usernames:
#         print("Access Granted")
#     else:
#         print("Access Denied")
# main()