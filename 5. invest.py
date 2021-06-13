def invest(amount, rate, years):
    for year in range(years):
        amount = amount + amount * rate
        print(f"Year {year}: ${amount:.2f}")

amount = float(input("Enter initial amount: "))
rate = float(input("Enter rate: "))
years = int(input("Enter years: "))
invest(amount, rate, years)
