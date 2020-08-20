def init():
    print("This is a simple calculator, enter an equation and it'll be calculated, you can also perform operations on "
          "the number stored in memory")
    return 0


def inputHandling():
    calcInput = input("Enter a calculation: ")
    calcInput = calcInput.replace(" ", "")
    if ifExitTrue(calcInput):
        return False
    return list(calcInput)


def whichOperation(aList):
    if "+" in aList:
        return 1
    elif "-" in aList:
        return 2
    elif "*" in aList:
        return 3
    elif "/" in aList:
        return 4


def addition(aList, memory):
    operandIndex = aList.index("+")
    if operandIndex == 0:
        memory += int("".join(aList[operandIndex + 1]))
        return memory
    else:
        return int("".join(aList[:operandIndex])) + int("".join(aList[operandIndex + 1::]))


def subtract(aList, memory):
    operandIndex = aList.index("-")
    if operandIndex == 0:
        memory -= int("".join(aList[operandIndex + 1]))
        return memory
    else:
        return int("".join(aList[:operandIndex])) - int("".join(aList[operandIndex + 1::]))


def multiply(aList, memory):
    operandIndex = aList.index("*")
    if operandIndex == 0:
        memory *= int("".join(aList[operandIndex + 1]))
        return memory
    else:
        return int("".join(aList[:operandIndex])) * int("".join(aList[operandIndex + 1::]))


def divide(aList, memory):
    operandIndex = aList.index("/")
    if operandIndex == 0:
        memory /= int("".join(aList[operandIndex + 1]))
        return memory
    else:
        return int("".join(aList[:operandIndex])) / int("".join(aList[operandIndex + 1::]))


def ifExitTrue(a):
    if "Exit" in a:
        print("Thank you for using my calculator")
        return True
    if "exit" == a:
        return True


memory = init()
while True:
    inputList = inputHandling()
    if not inputList:
        break
    if whichOperation(inputList) == 1:
        memory = addition(inputList, memory)
    elif whichOperation(inputList) == 2:
        memory = subtract(inputList, memory)
    elif whichOperation(inputList) == 3:
        memory = multiply(inputList, memory)
    else:
        memory = divide(inputList, memory)

    print(memory)
