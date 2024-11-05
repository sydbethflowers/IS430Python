"""Convert US dollars to other currencies."""


def main():
    us_dollars = eval(input('Please enter an amount in U.S. Dollars: '))
    euros = f"{us_dollars * 0.8815} Euros"
    china_yuan = f"{us_dollars * 6.3385} China Yuan"
    rupees = f"{us_dollars * 74.3827} India Rupees"
    pounds = f"{us_dollars * 0.7376} UK Pounds"
    canada_dollars = f"{us_dollars * 1.2581} Canada Dollars"
    money_conversions = [euros, china_yuan, rupees, pounds, canada_dollars]
    print(f"{us_dollars} in U.S. Dollars may be exchanged for:")
    print()
    for money in money_conversions:
        print(money)


main()
