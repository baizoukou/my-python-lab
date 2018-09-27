## using try accept out help the prog not to break
## basically it helps the program
## when debugging use specific err

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
