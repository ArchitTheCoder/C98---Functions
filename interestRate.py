def interestRate():
    principal = int(input("What is the principal (cost): "))
    rate = int(input("What is the interest rate (in percent): "))
    time = int(input("How long will this take (in months)? "))

    payment = principal * (1 + (rate/100 * time))
    interest = payment - principal

    print(f"You will have {str(interest)} in interest in {str(time)} months")

interestRate()