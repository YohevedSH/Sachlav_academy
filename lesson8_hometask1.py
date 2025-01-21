value = int(input("Enter a number "))
print("Fizzbuzz") if value % 3 == 0 and value % 5 == 0 else print(value)
if value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)