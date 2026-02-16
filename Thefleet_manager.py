# ---------------------------------
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