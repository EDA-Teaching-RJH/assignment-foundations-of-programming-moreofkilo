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
