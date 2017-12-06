import os, django, sys
sys.path.append('/home/mayur/Projects/restaurantWeb')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurantWeb.settings")
django.setup()

import json, datetime

from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from restaurantWeb.models import Customer,Dish,Order,CustomerPaymentMapping,Coupon,Restaurant


# we import the Twilio client from the dependency we just installed
from twilio.rest import Client


def get_user_to_send_message():
    customer_payment_mappings = CustomerPaymentMapping.objects.all()

    customer_payment_mapping_list = []  
    for customer_payment_mapping in customer_payment_mappings:
        remaining_timedelta = customer_payment_mapping.end_date - datetime.datetime.today().date()
        remaining_days = remaining_timedelta.days

        if remaining_days <= 3:
            customer_payment_mapping_list.append(customer_payment_mapping)

    return customer_payment_mapping_list


def send_message():
    customer_payment_mapping_list = get_user_to_send_message()
    client = Client("AC946d780d63ba48efb3fdaab93cb6f4cb", "d27da6a96fc520a1e5254e4c3c2dc48d")

    for customer_payment_mapping in customer_payment_mapping_list:
        contact_no = '+91'+str(customer_payment_mapping.customer.customer_contact)
        message = "Your monthly subscription for the restaurant is about to end. Please make payment to renew the service"

        try:
            client.messages.create(to=contact_no, from_="+18312915447", body=message)
        except Exception as e:
            print e
            print 'Cannot send sms to {}'.format(contact_no)


if __name__ == '__main__':
    send_message()