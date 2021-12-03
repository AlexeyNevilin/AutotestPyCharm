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






    ''''my_date = datetime.strptime(my_date, '%d.%m.%y')
    my_date = datetime.date(my_date)
    if my_month > 0:
        my_month = str(my_month)
        my_month = datetime.strptime(my_month, '%m')
        my_month = datetime.date(my_month)
        print(my_month)
        new_date = my_date + my_month.month
        print(new_date)
    else:
        my_month = my_month * (-1)
        my_month = datetime.strptime(my_month, '%m')
        my_month = datetime.date(my_month)
        new_date = my_date - my_month
        print(new_date)'''
    '''new_date = my_date.month - my_date.month
    print(new_date)
    new_date = my_date.month + my_month
    print(new_date)'''


"""my_data = '12.12.12'
my_month = -5
print(datetime.date(my_data))"""
# def change_month(my_data, my_month):
# print(datetime.date(my_data) + datetime.timedelta(my_month.month))


'''def change_month(my_data, numb_month):
    my_data = datetime.date(my_data.year + (math.ceil((my_data.month / 12) if (my_data.month / 12) > 0 else math.floor((my_data.month / 12)), (my_data.month - numb_month), my_data.day)
    print(my_data)'''

'''next_date = datetime.date(my_data.year + int(my_data.month / 12 + numb_month / 12), (my_data.month + numb_month) % 12, my_data.day)
print(next_date) '''

'''def change_month(mydate, months):
    skip_months = datetime.datetime(mydate.year + int(months / 12), (mydate.month % 12 + months % 12), 1)
    skip_months = skip_months + datetime.timedelta(days=mydate.day)
    print(skip_months)'''
