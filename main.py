def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiple(x, y):
    return x * y


def divide(x, y):
    return x / y


print("1.add , 2.subtract , 3.multple , 4.divide")


while True:
    user_choice = input("select by picking the number: ")
    if user_choice in ('1,','2','3','4'):
        first = int(input("enter first: "))
        second = int(input("enter second: "))
        if user_choice == '1':

            print(add(first, second)," is your answer")

        elif user_choice == '2':
            print(subtract(first, second), " is your answer")

        elif user_choice == '3':
            print(multiple(first, second), " is your answer")

        elif user_choice == '4':
            print(divide(first, second), " is your answer")

        next_choice = input("another calculation yes or no: ")
        if next_choice == "no":
            break
        else:
         print("invaild choice")
