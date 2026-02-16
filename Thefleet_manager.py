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
