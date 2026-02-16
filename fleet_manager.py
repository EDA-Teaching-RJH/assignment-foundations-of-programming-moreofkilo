def init_database():
    crew_names = [
        "Jean-Luc Picard",
        "William Riker",
        "Geordi La Forge",
        "Data",
        "Deanna Troi"
    ]

    crew_ranks = [
        "Captain",
        "Commander",
        "Lieutenant",
        "Lieutenant Commander",
        "Commander"
    ]

    crew_divs = [
        "Command",
        "Command",
        "Operations",
        "Operations",
        "Sciences"
    ]

    crew_ids = ["NCC01", "NCC02", "NCC03", "NCC04", "NCC05"]

    return crew_names, crew_ranks, crew_divs, crew_ids


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


def add_member(names, ranks, divs, ids):
    print("\n-- Add New Crew --")

    new_id = input("Assign ID: ").upper()

    if new_id in ids:
        print("ERROR: ID already exists.")
        return

    valid_ranks = [
        "Captain", "Commander",
        "Lieutenant Commander",
        "Lieutenant", "Ensign", "Admiral"
    ]

    new_rank = input("Rank: ")

    if new_rank not in valid_ranks:
        print("ERROR: Invalid Starfleet rank.")
        return

    new_name = input("Name: ")
    new_div = input("Division: ")

    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)

    print("Crew member successfully added.")



def remove_member(names, ranks, divs, ids):
    print("\n-- Remove Crew --")
    target = input("Enter ID: ").upper()

    if target not in ids:
        print("Crew ID not located.")
        return

    pos = ids.index(target)

    del names[pos]
    del ranks[pos]
    del divs[pos]
    del ids[pos]

    print("Crew member deleted.")



def update_rank(names, ranks, ids):
    print("\n-- Rank Update --")
    target = input("Enter ID: ").upper()

    if target in ids:
        pos = ids.index(target)
        print("Current:", names[pos], "-", ranks[pos])
        new_rank = input("New Rank: ")
        ranks[pos] = new_rank
        print("Rank updated successfully.")
    else:
        print("No matching ID found.")



def display_roster(names, ranks, divs, ids):
    print("\n========= CREW ROSTER =========")

    if len(names) == 0:
        print("No crew recorded.")
        return

    header = f"{'ID':<8}{'NAME':<25}{'RANK':<22}{'DIVISION':<15}"
    print(header)
    print("-" * len(header))

    for i in range(len(names)):
        line = f"{ids[i]:<8}{names[i]:<25}{ranks[i]:<22}{divs[i]:<15}"
        print(line)



def search_crew(names, ranks, divs, ids):
    print("\n-- Crew Search --")
    term = input("Search name: ").lower()
    hit = False

    for i in range(len(names)):
        if term in names[i].lower():
            print(ids[i], "|", names[i], "|", ranks[i], "|", divs[i])
            hit = True

    if not hit:
        print("No results found.")



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


def calculate_payroll(ranks):
    pay = {
        "Admiral": 1500,
        "Captain": 1000,
        "Commander": 800,
        "Lieutenant Commander": 600,
        "Lieutenant": 400,
        "Ensign": 200
    }

    total_cost = 0

    for r in ranks:
        if r in pay:
            total_cost += pay[r]

    return total_cost



def count_officers(ranks):
    total = 0
    for r in ranks:
        if r in ("Captain", "Commander"):
            total += 1
    return total



def main():
    names, ranks, divs, ids = init_database()

    while True:
        option = display_menu()

        if option == "1":
            add_member(names, ranks, divs, ids)

        elif option == "2":
            remove_member(names, ranks, divs, ids)

        elif option == "3":
            update_rank(names, ranks, ids)

        elif option == "4":
            display_roster(names, ranks, divs, ids)

        elif option == "5":
            search_crew(names, ranks, divs, ids)

        elif option == "6":
            filter_by_division(names, divs)

        elif option == "7":
            total = calculate_payroll(ranks)
            print("Total Payroll:", total, "credits")

        elif option == "8":
            num = count_officers(ranks)
            print("Senior Officers:", num)

        elif option == "9":
            print("System logging off...")
            break

        else:
            print("Invalid selection.")