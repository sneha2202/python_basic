def calc():
    cont='y'
    while (cont=='y'):
        num = input("Enter your CGPA : ")

        if float(num) >= 4 and float(num) <= 4.74:
            print("Grade D")
            calculate = (6.6 * float(num) + 13.6)
            print("Your Percentage is : ", calculate)

        elif float(num) >= 4.75 and float(num) <= 5.74:
            print("Grade B")
            calcu = (10 * float(num) - 2.5)
            print("Your Percentage is : ", calcu)

        elif float(num) >= 5.75 and float(num) <= 6.74:
            print("Grade B+")
            formula = (5 * float(num) + 26.25)
            print("Your Percentage is : ", formula)

        elif float(num) >= 6.75 and float(num) <= 8.24:
            print("Grade A")
            form = (6.6 * float(num) + 13.6)
            print("Your Percentage is : ", form)

        elif float(num) >= 8.25 and float(num) <= 9.49:
            print("Grade A+")
            use = (12 * float(num) - 25)
            print("Your Percentage is : ", use)

        elif float(num) >= 9.50 and float(num) <= 10.00:
            print("Grade O")
            cal = (20 * float(num) - 100)
            print("Your Percentage is : ", cal)

        elif (int(num) < 4 or int(num) > 10):
            print("Please enter your number in between 4 to 10.00")


        cont = input("Would you like to continue (y/n) : ")


calc()
