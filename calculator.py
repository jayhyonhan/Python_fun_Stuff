while True:
    num1, num2 = input("please enter two numbers : ").split()
    calculateWay = input("please enter \"plus\", \"minus\", \"multiply\", or \"divide\" : ")

    if calculateWay == "plus":
        print(int(num1) + int(num2))
    elif calculateWay == "minus":
        print(int(num1) - int(num2))
    elif calculateWay == "multiply":
        print(int(num1) * int(num2))
    elif calculateWay == "divide":
        print(int(num1) / int(num2))
    else:
        pass
