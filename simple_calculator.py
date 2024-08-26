def simple_calculator():
    if choice.lower() == "addition":
        V3 = V1 + V2
    elif choice.lower() == "subtraction":
        if V1>V2:
            V3 = V1 - V2
        else:
            V3 = V2 - V1
    elif choice.lower() == "multiplication":
        V3 = V2*V1
    elif choice.lower() == "division":
        choice2 = input("Do you want the first value to divide second value yes/no? ")
        if choice2.lower() == "yes":
            V3 = V1 / V2 
        elif choice2.lower() == "no":
            V3 = V2/V1
    else:
        print("Input is not valid, type a correct input")
        return
    print('The result of the ', choice.lower(), ': ', V3)
V1 = int(input("Input first value: "))
V2 = int(input("Input second value: "))
choice = input("Do you want to perform addition, subtraction, multiplication or division? ")
simple_calculator()



