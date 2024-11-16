# Умовні конструкції
# Task 1

rightPassword = "password123"
userPassword = input("Введіть ваш пароль: ")

if rightPassword == userPassword:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

# Task 2

dayNumber = int(input("Choose number from 1 to 7: "))
if dayNumber < 1 or dayNumber > 7:
    print("Error, invalid data")
else:
    if dayNumber == 1:
        print("Monday")
    elif dayNumber == 2:
        print("Tuesday")
    elif dayNumber == 3:
        print("Wednesday")
    elif dayNumber == 4:
        print("Tursday")
    elif dayNumber == 5:
        print("Friday")
    elif dayNumber == 6:
        print("Saturday")
    else:
        print("Sunday")