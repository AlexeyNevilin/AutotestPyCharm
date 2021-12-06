from datetime import datetime, date
from dateutil.relativedelta import relativedelta
#change_month('21.06.17', -5)
def change_month(my_date, my_month):
    my_date = datetime.strptime(my_date, '%d.%m.%y').date()
    change_date = my_date + relativedelta(months=+my_month)
    print(change_date.strftime('%d.%m.%y'))


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