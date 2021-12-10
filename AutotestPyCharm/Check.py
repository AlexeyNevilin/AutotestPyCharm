# change_month(datetime.datetime(2005, 6, 15), 6) change_month(datetime.date(2005, 6, 15), 5)
from datetime import datetime
from datetime import timedelta

# change_month('21.06.17', -5)
def change_month(input_date, input_month):
    date = datetime.strptime(input_date, '%d.%m.%y').date()
    if (date.month + input_month) % 12 == 0:
        modified_month = 12
    else:
        modified_month = (date.month + input_month) % 12
    modified_year = date.year

    month = date.month + input_month
    if month > 12:
        while month > 12:
            month -= 12
            modified_year += 1
    elif month <= 0:
        while month <= 0:
            month += 12
            modified_year -= 1
    else:
        modified_year = date.year

    modified_year_str = str(date.day).zfill(2) + '.' + str(modified_month).zfill(2) + '.' + str(modified_year).zfill(2)
    if 28 <= date.day <= 31 and modified_month != 12:
        max_day = datetime.strptime(('01' + '.' + str(modified_month + 1).zfill(2) + '.' + str(modified_year).zfill(2)), '%d.%m.%Y').date() - timedelta(days=1)
        max_day = str(max_day.day).zfill(2) + '.' + str(max_day.month).zfill(2) + '.' + str(max_day.year).zfill(2)
        if modified_year_str > max_day:
            max_day = datetime.strptime(max_day, '%d.%m.%Y').date()
            modified_day = max_day.day
        else:
            modified_day = date.day
    else:
        modified_day = date.day

    modified_date = str(modified_day).zfill(2) + '.' + str(modified_month).zfill(2) + '.' + str(modified_year).zfill(2)
    modified_date = datetime.strptime(modified_date, '%d.%m.%Y').date()
    print(modified_date)


