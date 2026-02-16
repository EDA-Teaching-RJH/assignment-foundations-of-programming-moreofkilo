# ---------------------------------
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
