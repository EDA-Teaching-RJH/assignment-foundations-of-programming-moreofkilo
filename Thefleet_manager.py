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
