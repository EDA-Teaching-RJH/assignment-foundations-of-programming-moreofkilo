def filter_by_division(names, divs):
    print("\n-- Division Filter --")
    choice = input("Division: ")

    found = False
    for i in range(len(names)):
        if divs[i].lower() == choice.lower():
            print(names[i], "-", divs[i])
            found = True

    if not found:
        print("No crew in that division.")
