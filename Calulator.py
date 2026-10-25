def calculator():
    print("====SIMPLE CALCULATOR====")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")
    print("5.Exit")

    while True:
        choice=input("\nEnter your choice(1-5):")

        if choice == "5":
            print("Thank You for using calculator!")
            break

        if choice not in ["1","2","3","4"]:
            print("Invalid choice! Try again")
            continue

        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))

        if choice=="1":
            print("Result:",a+b)

        elif choice=="2":
             print("Result:",a-b)

        elif choice=="3":
             print("Result:",a*b)

        elif choice=="4":
             if b==0:
                 print("Cannot divide by zero")
             else:
                print("Result:",a/b)

calculator()

            





