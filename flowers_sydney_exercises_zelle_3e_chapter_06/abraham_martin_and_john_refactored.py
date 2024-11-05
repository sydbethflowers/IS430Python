"""
Using a common function to format dates this program prints the name,
date of birth, and date of death of the four key figures
mentioned in the song "Abraham, Martin and John" by Dick Holler:

    Abraham Lincoln
    Martin Luther King Jr.
    John F. Kennedy
    Robert F. Kennedy
"""
# source: https://en.wikipedia.org/wiki/Abraham,_Martin_and_John


def main():
    key_figure_facts = [
        ('Abraham Lincoln', '1809-02-12', '1865-04-15'),
        ('Martin Luther King Jr.', '1929-01-15', '1968-04-04'),
        ('John F. Kennedy', '1917-05-29', '1963-11-22'),
        ('Robert F. Kennedy', '1925-11-20', '1968-06-06')
    ]

    print('Key Figures from the Song "Abraham, Martin and John" by Dick Holler:')
    for fact_tuple in key_figure_facts:
        name, date_of_birth, date_of_death = fact_tuple
        print()
        print(name)
        print(f'Born: {format_dates(date_of_birth)}')
        print(f'Died: {format_dates(date_of_death)}')


def format_dates(date):
    return f"{date[5:7]}/{date[8:10]}/{date[0:4]}"


main()
