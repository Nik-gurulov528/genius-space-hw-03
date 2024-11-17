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

# Цикли

# Task 1

sheet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
userNumber = int(input("Your number please: "))
for num in sheet:
    print(f"{userNumber} * {num} = ", userNumber * num)

# Task 2

numberOfNumbers = int(input("How many numbers do you want to calculate? "))
i = 1
lst = []
totalNum = 0
while i <= numberOfNumbers:
    lst.append(input("Enter number: "))
    i += 1
for num in lst:
    totalNum += int(num)
print(totalNum)

# Task 3

startNumber = int(input("Enter your number: "))
listOfNumbers = []
endNumber = 1
while startNumber > 0:
    listOfNumbers.append(startNumber)
    startNumber -= 1
for num in listOfNumbers:
    endNumber *= num
print(endNumber)

# Task 4

numberArray = []
beginNumber = 1
while beginNumber <= 50:
    numberArray.append(beginNumber)
    beginNumber += 1
for num in numberArray:
    if num % 2 == 0:
        print(num)

# Task 5

beginOfRange = int(input("Enter first number of list: "))
endOfRange = int(input("Enter last number of list: "))
if beginOfRange != 1:
    array = [1]
else:
    array = []
i = beginOfRange
numberOfRemainders = 0
while i >= beginOfRange and i <= endOfRange:
    array.append(i)
    i += 1
for num in array:
    for number in array:
        if num % number == 0:
            numberOfRemainders += 1
    if numberOfRemainders > 2:
        numberOfRemainders = 0
    else:
        if num != 1:
            print(num)
        numberOfRemainders = 0