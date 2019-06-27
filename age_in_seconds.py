import datetime
# from datetime import date

def calculateAgeInSeconds(DoB):
    current_date = datetime.datetime.today()
    # print("Today's date:", current_date)
    result = current_date - DoB
    seconds = (((result.days * 24) * 60) * 60)
    
    return seconds


def main():
    date_entry = input('Enter a date in DD/MM/YYYY format: ')
    day, month, year = map(int, date_entry.split('/'))
    date1 = datetime.datetime(year, month, day)
    print('Age in seconds = ', calculateAgeInSeconds(date1))


main()

