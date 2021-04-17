def eligibility():
    age = int(input("How old are you? "))

    if age >= 18:
        print("You are eligible to vote")
    else:
        diff = 18 - age
        print(f"You need to wait {str(diff)} more years to vote")

eligibility()