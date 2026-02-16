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