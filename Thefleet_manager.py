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