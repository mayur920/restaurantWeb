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

def get_user_to_send_email():
	