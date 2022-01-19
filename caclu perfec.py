count = False

num1 = int(input("what is your first num"))

num2 = int(input("what is your second num"))

choice = int(input(" 1 to add, 2 to subtract  3 to divide 4 to multiply"))

while count == False:
    add = num1+num2
    subtract = num1-num2
    multi = num1*num2
    div = num1/num2
    if choice==1:
        print(add)
    elif choice==2:
        print(subtract)
    elif choice==3:
        print(div)
    else:
        print(multi)

    num1 = int(input("what is your first num"))

    num2 = int(input("what is your second num"))

    choice = int(input(" 1 to add, 2 to subtract  3 to divide 4 to multiply"))

