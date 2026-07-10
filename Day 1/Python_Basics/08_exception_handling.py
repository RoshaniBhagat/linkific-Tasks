try:
    num = int(input("Enter a number: "))
    print(100 / num)

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program Finished")
    