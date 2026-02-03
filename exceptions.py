"""
Error Handling Practice in Python
Author: Aaditya
Description:
This file contains examples demonstrating Python error handling using
try, except, else, finally, break, and continue.
"""


# --------------------------------------------------
# 1. Basic try / except
# --------------------------------------------------

def basic_try_except():
    try:
        x = int(input("Enter a number: "))
        print(f"You entered: {x}")
    except ValueError:
        print("That was not a valid number")


# --------------------------------------------------
# 2. Catching a specific exception
# --------------------------------------------------

def file_read_example():
    try:
        file = open("data.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found")
    finally:
        # Cleanup
        try:
            file.close()
        except NameError:
            pass


# --------------------------------------------------
# 3. finally runs even with break
# --------------------------------------------------

def break_with_finally():
    while True:
        file = None
        try:
            file = open("data.txt", "r")
            print("File opened successfully")
            break
        except FileNotFoundError:
            print("File not found")
            break
        finally:
            print("Finally block executed")
            if file:
                file.close()


# --------------------------------------------------
# 4. try / except / else pattern
# --------------------------------------------------

def ask_number_and_square():
    while True:
        try:
            num = int(input("Input an integer: "))
            square = num ** 2
            print(f"Thank you, your number squared is: {square}")
        except ValueError:
            print("An error occurred! Please try again!")
            continue
        else:
            # Runs only if no exception occurred
            break


# --------------------------------------------------
# 5. continue skips current iteration
# --------------------------------------------------

def continue_example():
    for i in range(5):
        if i == 2:
            continue
        print(i)


# --------------------------------------------------
# 6. break inside except (finally still runs)
# --------------------------------------------------

def break_inside_except():
    while True:
        try:
            x = int("abc")  # Will raise ValueError
        except ValueError:
            print("Error occurred")
            break
        finally:
            print("Finally block executed")


# --------------------------------------------------
# 7. continue inside try (finally still runs)
# --------------------------------------------------

def continue_inside_try():
    count = 0
    while count < 3:
        try:
            print("Try block")
            count += 1
            continue
        finally:
            print("Finally block")


# --------------------------------------------------
# 8. Pythonic version using return
# --------------------------------------------------

def ask_pythonic():
    while True:
        try:
            return int(input("Enter a number: ")) ** 2
        except ValueError:
            print("Please enter a valid integer")


# --------------------------------------------------
# Entry point for testing
# --------------------------------------------------

if __name__ == "__main__":
    # Uncomment functions to test them one by one

    # basic_try_except()
    # file_read_example()
    # break_with_finally()
    # ask_number_and_square()
    # continue_example()
    # break_inside_except()
    # continue_inside_try()

    result = ask_pythonic()
    print(f"Result from pythonic function: {result}")
