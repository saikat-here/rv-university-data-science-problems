"""
The Python programming language is a great tool to use when working with numbers and evaluating mathematical expressions. This quality can be utilized to make useful programs.
In this assignment,you will be learning how to make a calculator program in Python. This calculator will be able to perform various mathematical/arithmetic operations, but the final step of this guide serves as a starting point for how you might improve the code to create a more robust calculator.
The goal is to create a simple calculator which can perform basic arithmetic operations like addition, subtraction, multiplication or division depending upon the user input.
"""

def take_input(minNum = 2, maxNum = None):
    """
    Used to take user inputs
    Args:
      minNum: count of minimum number. Like for addition, min number count should be 2
      maxNum: count of max number. Like for division, we are considering max 2 numbers.
    """
    operation_input = []

    count = 1
    while True:
        try:
            n = float(input("Please enter the number: "))
            operation_input.append(n)

            if minNum != None and count < minNum: # Checking for ofr min number count requirement
                count += 1
                continue
            if maxNum != None and count == maxNum: # checking for the max number count requirement
                break

            newNumber = input \
                ("Do you want to enter another number YES/NO? (Default is YES): ") or "YES" # default/no input value of this input in YES
            if newNumber.lower() == "no":
                break
        except ValueError:  # converstion will throw exception if other than number privided, catching that
            print("Invalid number, please enter again")
            continue
    return operation_input


def add():
    """
    Performs the addition"
    """
    operation_input = take_input()
    res = 0
    for i in operation_input:
        res += i
    return res

def sub():
    """
    Performs the subtraction operation
    """
    operation_input = take_input()
    res = operation_input[0]
    for i in operation_input[1:]:
        res -= i
    return  res

def multi():
    """
    Performs the multiplication operation
    """
    operation_input = take_input()
    res = 1
    for i in operation_input:
        res *= i
    return res

def div():
    """
    Performs division operation
    """
    operation_input = take_input(minNum=2, maxNum=2)

    if operation_input[1] == 0:
        return "Infinite"

    return operation_input[0] / operation_input[1]


while True:

    # printing the meni for operations
    operation = input \
        ("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit \n\nPlease select the operation:")

    # checking if the entered option is correct
    if operation not in ["1" ,"2" ,"3" ,"4" ,"5"]:
        print("Invalid operation selected. Please select a correct one")
        continue

    # calling the methods depending on the operation selected
    if operation == "1":
        print(f"\nResult: {add()}\n")

    elif operation == "2":
        print(f"\nResult: {sub()}\n")

    elif operation == "3":
        print(f"\nResult: {multi()}\n")

    elif operation == "4":
        print(f"\nResult: {div()}\n")

    elif operation == "5":
        break # breaking on Exit menu selction
