from datetime import datetime

def calculateAgeInSeconds(DoB):
    current_date = datetime.today()
    result = DoB - current_date
    return result


def main():
    date_entry = input('Enter a date in YYYY-MM-DD format')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.datetime(year, month, day)
    print(calculateAgeInSeconds(date1))


main()

