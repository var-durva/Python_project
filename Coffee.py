while True:
    coffee = input("Enter coffee status: ").strip().lower()
    if coffee == "empty":
        print("Fill")
        break
    elif coffee == "full":
        print("Drink")
        break
    else:
        print("it's ok")
    pass
print("So proceed ....")