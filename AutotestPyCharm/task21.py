from datetime import datetime

#change_month('21.06.17', -5)
def change_month(my_date, my_month):
    my_date = datetime.strptime(my_date, '%d.%m.%y').date()
    change_date_day = my_date.day
    if (my_date.month + my_month) % 12 == 0:
        change_date_month = 12
    else:
        change_date_month = (my_date.month + my_month) % 12
    change_date_year = my_date.year
    year_numb = my_date.month + my_month
    if year_numb > 12:
        while year_numb > 12:
            year_numb -= 12
            change_date_year += 1
    elif year_numb <= 0:
        while year_numb <= 0:
            year_numb += 12
            change_date_year -= 1
    else:
        change_date_year = my_date.year
    print(str(change_date_day).zfill(2) + '.' + str(change_date_month).zfill(2) + '.' + str(change_date_year).zfill(2))

'''from datetime import datetime, date
from dateutil.relativedelta import relativedelta
#change_month('21.06.17', -5)
def change_month(my_date, my_month):
    my_date = datetime.strptime(my_date, '%d.%m.%y').date()
    change_date = my_date + relativedelta(months=+my_month)
    print(change_date.strftime('%d.%m.%y'))'''


'''
# change_month(datetime.datetime(2005, 6, 15), 6) change_month(datetime.date(2005, 6, 15), 5)
from datetime import datetime

#change_month('21.06.17', -5)
def change_month(my_date, my_month):
    my_date = datetime.strptime(my_date, '%d.%m.%y').date()
    if my_month > 0:
        new_date = (
            str(my_date.day).zfill(2)
            + '.' +
            (str(my_date.month + my_month) if (my_date.month + my_month) <= 12 else str((my_date.month + my_month) % 12)).zfill(2)
            + '.' +
            (str(my_date.year + 0) if (my_month + my_date.month) <= 12 else str(my_date.year + ((my_date.month + my_month) // 12)))
        )
        print(new_date)
    else:
        new_date = (
            str(my_date.day).zfill(2)
            + '.' +
            (str(my_date.month + my_month) if (my_date.month + my_month) > 0 else str((my_date.month + my_month) // 12)).zfill(2)
            + '.' +
            (str(my_date.year + 0) if (my_date.month + my_month) > 0 else str(my_date.year + ((my_date.month + my_month) // 12)))
        )
        print(new_date)
'''