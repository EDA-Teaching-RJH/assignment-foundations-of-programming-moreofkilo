def count_officers(ranks):
    total = 0
    for r in ranks:
        if r in ("Captain", "Commander"):
            total += 1
    return total