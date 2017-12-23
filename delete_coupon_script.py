import os, django, sys, json, datetime, calendar
sys.path.append('/home/mayur/Projects/restaurantWeb')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurantWeb.settings")
django.setup()


from restaurantWeb.models import Coupon
from django.http import JsonResponse

def delete_coupon():
    first_day,last_day,current_month_last_day_date == get_date_range()

    print 'first_Day of previous month:',first_day
    print 'last_day of previous month:',last_day
    print 'last day of current_month:',current_month_last_day_date

    if datetime.datetime.today().day != current_month_last_day_date:
        return 'None,because today not a last day of month'
        print None

    coupons = Coupon.objects.filter(coupon_date_range=(first_day,last_day)).delete()

    print 'coupons removed'

    return 'coupons removed'

def get_date_range():
    today = datetime.datetime.today()
    previous_month = today.month-1 if today.month-1 != 0 else 12
    current_month = today.month
    current_year = today.current_year
    current_month_date_range = calendar.monthrange(current_year,current_month)
    year = today.year

    if previous_month == 12:
        year = today.year-1
    month_date_range = calendar.monthrange(year,previous_month)
    last_day_date = month_date_range[1]
    current_month_last_day_date = current_month_date_range[1]

    first_day = datetime.date(year,previous_month,1)
    last_day = datetime.date(year,previous_month,last_day_date)

    return first_day,last_day,current_month_last_day_date


if __name__ == '__main__':
    delete_coupon()