# change_month(datetime.datetime(2005, 6, 15), 6) change_month(datetime.date(2005, 6, 15), 5)
from datetime import datetime

#change_month('21.06.17', -5)
def change_month(my_date, my_month):
    my_date = datetime.strptime(my_date, '%d.%m.%y').date()
    change_date_day = my_date.day
    change_date_month = (my_date.month + my_month) % 12
    change_date_year = my_date.year
    year_numb = my_date.month + my_month
    if year_numb > 12:
        while year_numb > 12:
            year_numb - 12
            print(year_numb, '1')
            #change_date_year = my_date.year + 1
        #change_date_year = change_date_year
    elif year_numb <= 0:
        while year_numb <= 0:
            year_numb + 12
            print(year_numb, '2')
            #change_date_year = my_date.year - 1
        #change_date_year = change_date_year
    else:
        change_date_year = my_date.year
        print(year_numb, '3')
    print(year_numb, '4')
    print(change_date_day)
    print(change_date_month)
    print(change_date_year)


    '''my_month2 = (my_date.month + my_month) / 12
    my_month3 = (my_date.month + my_month) // 12
    print('my_month', my_month)
    print('my_month2', my_month2)
    print('my_month3' ,my_month3)
    print(my_date_month)'''