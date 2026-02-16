def display_menu():
    user = input("\nEnter officer name: ")

    print("\n========== FLEET CONTROL ==========")
    print("Active Officer:", user)
    print("1 - Add Crew Member")
    print("2 - Remove Crew Member")
    print("3 - Update Rank")
    print("4 - Show Roster")
    print("5 - Search Crew")
    print("6 - Division Filter")
    print("7 - Payroll Total")
    print("8 - Officer Count")
    print("9 - Exit Program")

    return input("Select option: ")
