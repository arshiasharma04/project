#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = int(input('''\t\tpress 1 to calculate BMI
                press 2 to convert temperaturer
                press 3 to calculate age
                press 4 to see calendar
                press 5 to roll dice
                press 6 to use arithmetic calculator+
                press 7 to generate random password'''))
if n == 1:

    height = float(input("Enter Your Height in cm:"))
    weight = float(input("Enter Your Weight in Kg:"))

    height = height / 100

    BMI = weight / (height * height)

    print("Your Body Mass Index is:", BMI)
    if BMI > 0:

        if BMI <= 16:

            print("You are Severely Underweight")

        elif BMI <= 18.5:
            print("You are underweight")

        elif BMI <= 25:
            print("You are Healthy")

        elif BMI <= 30:
            print("You are Overweight")

        else:
            print("very very high!")
elif n == 2:

    n = int(input("for fahrenheit to celsius=1,celsius to fahrenheit=2"))
    if n == 1:
        Fahrenheit = int(input("Enter the Value of Fahrenheit:"))

        celsius = (Fahrenheit - 32) * 5 / 9

        print("celsius Value:", celsius)

    elif n == 2:
        celsius = int(input("Enter the Value of celsius:"))

        Fahrenheit = (celsius * (9 / 5)) + 32

        print("Fahrenheit Value:", Fahrenheit)
    else:
        print("invalid operation")
elif n == 3:
    def ageCalculator(y, m, d):
        import datetime
        today = datetime.datetime.now().date()
        dob = datetime.date(y, m, d)
        age = int((today - dob).days / 365.25)
        print(age)


    y = int(input("Enter year of birth:"))
    m = int(input("Enter month of birth:"))
    d = int(input("Enter date of birth:"))
    ageCalculator(y, m, d)
elif n == 4:
    import calendar

    year = int(input("Enter the year:"))
    cal = calendar.calendar(year)
    print(cal)
elif n == 5:
    import random

    x = "y"

    while x == "y":
        random_number = random.randint(1, 6)

        if random_number == 1:
            print("[---------]")
            print("[         ]")
            print("[    *    ]")
            print("[         ]")
            print("[---------]")

        elif random_number == 2:
            print("[---------]")
            print("[  *      ]")
            print("[         ]")
            print("[      *  ]")
            print("[---------]")

        elif random_number == 3:
            print("[---------]")
            print("[         ]")
            print("[ *  *  * ]")
            print("[         ]")
            print("[---------]")

        elif random_number == 4:
            print("[---------]")
            print("[ *     * ]")
            print("[         ]")
            print("[ *     * ]")
            print("[---------]")

        elif random_number == 5:
            print("[---------]")
            print("[ *     * ]")
            print("[    *    ]")
            print("[ *     * ]")
            print("[---------]")

        elif random_number == 6:
            print("[---------]")
            print("[ *  *  * ]")
            print("[         ]")
            print("[ *  *  * ]")
            print("[---------]")

        x = input("Press y to Roll Again and Press Any Other Key for Exit:")
elif n == 6:
    num1 = int(input("Enter the First Number:"))
    oper = input("Enter the Operation:")
    num2 = int(input("Enter the Second Number:"))

    if oper == "+":
        sum = num1 + num2
        print("The Answer is:", sum)

    elif oper == "-":
        subs = num1 - num2
        print("The Answer is:", subs)

    elif oper == "*":
        mul = num1 * num2
        print("The Answer is:", mul)

    elif oper == "/":
        div = num1 / num2
        print("The Answer is:", div)

    else:
        print("Wrong Operation Input!")

    print("=========================\n")
elif n == 7:
    import random

    passlen = int(input("Enter the Length of Password:"))
    x = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?<>"
    password = "".join(random.sample(x, passlen))
    print(password)

elif n>7:
    print("not applicable")


# In[ ]:





# In[ ]:




