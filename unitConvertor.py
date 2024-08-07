while True:
    value = float(input("Enter value of kilometer: "))

    print("To what you want to convert")
    print("1 for KM to Mile ")
    print("2 for KM to Meter ")

    unit = int(input("Enter 1 or 2: "))

    if unit==1:
        print(value*0.62)
    elif unit==2:
        print(value*1000)