upper_number = int(input("Enter a number from 1 to 30:"))
for number in range(0,upper_number + 1):
    if number % 4 == 0 and number % 7 == 0:
        print("Israel Forever")
    elif number % 4 == 0:
        print("Israel")
    elif number % 5 == 0:
        print("Forever")
    else:
        print(number)