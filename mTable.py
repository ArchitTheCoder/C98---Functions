def table():
    num = float(input("Enter the number: "))
    tableNum = num

    for i in range(10):
        print(tableNum)
        tableNum = tableNum + num

table()