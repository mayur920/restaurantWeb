# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import os, re
from restaurantWeb.settings import BASE_DIR

def upload_dish_image(instance, filename):
   if os.path.isdir(BASE_DIR+'/Media/Dishes') == True: # will go in if statement, if required directory is exist.
       return os.path.join('Dishes/'+"%s" %(re.sub('[^a-zA-Z0-9 \.\_]', '', filename).replace(' ', ''), ))
   else:
       os.makedirs(BASE_DIR+'/Media/Dishes')
       return os.path.join('Dishes/'+"%s" %(re.sub('[^a-zA-Z0-9 \.\_]', '', filename).replace(' ', ''), ))


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User)
    restaurant = models.ForeignKey('Restaurant',null=True)
    customer_address = models.CharField(max_length=300)
    customer_contact = models.IntegerField()

    def __unicode__(self):
        return "{} {} {} {}".format(self.id, self.user.first_name, self.user.last_name,
                                    self.customer_address, self.customer_contact
                                   )
    def get_json(self):
        result = {}
        result['id'] = self.id if self.id else None
        result['user_id'] = self.user.id if self.user else None
        result['first_name'] = self.user.first_name if self.user else None
        result['last_name'] = self.user.last_name if self.user else None
        result['restaurant_id'] = self.restaurant.id if self.restaurant else None
        result['restaurant_name'] = self.restaurant.restaurant_name if self.restaurant else None
        result['customer_address'] = self.customer_address if self.customer_address else None
        result['customer_contact'] = self.customer_contact if self.customer_contact else None

        return result

class Dish(models.Model):
    restaurant = models.ForeignKey('Restaurant',null=True)
    dish_name = models.CharField(max_length=100)
    dish_type = models.CharField(max_length=100)
    dish_pic = models.ImageField(upload_to = upload_dish_image)

    def __unicode__(self):
        return "{} {} {}".format(self.id, self.dish_name, self.dish_type, self.dish_pic)


    def get_json(self):
        result = {}
        result['id'] = self.id if self.id else None
        result['dish_name'] = self.dish_name if self.dish_name else None
        result['restaurant_id'] = self.restaurant.id if self.restaurant else None
        result['restaurant_name'] = self.restaurant.restaurant_name if self.restaurant else None
        result['dish_type'] = self.dish_type if self.dish_type else None
        result['dish_pic'] = self.dish_pic if self.dish_pic else None

        print result
        return result


class Order(models.Model):
    restaurant = models.ForeignKey('Restaurant', null=True)
    item_name = models.CharField(max_length=200)
    item_no = models.IntegerField()
    order_address = models.CharField(max_length=300)

    def __unicode__(self):
        return "{} {} {}".format(self.id, self.item_name, self.item_no, self.order_address)

    def get_json(self):
        result = {}
        result['id'] = self.id if self.id else None
        result['item_name'] = self.item_name if self.item_name else None
        result['restaurant_id'] = self.restaurant.id if self.restaurant else None
        result['restaurant_name'] = self.restaurant.restaurant_name if self.restaurant else None
        result['item_no'] = self.item_no if self.item_no else None
        result['order_address'] = self.order_address if self.order_address else None

        print result
        return result

class CustomerPaymentMapping(models.Model):
    restaurant = models.ForeignKey('Restaurant',null=True)
    customer = models.ForeignKey('Customer',null=True)
    payment_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    payment_date = models.DateField()
    customer_amount = models.FloatField()


    def __unicode__(self):
        return "{} {}".format(self.id, self.payment_type, self.payment_date,
                              self.start_date,self.end_date, self.customer_amount)

    def get_json(self):
        result = {}
        result['id'] = self.id if self.id else None
        result['customer_id'] = self.customer.id if self.customer else None
        result['customer_fname'] = self.customer.customer_fname if self.customer else None
        result['restaurant_id'] = self.restaurant.id if self.restaurant else None
        result['restaurant_name'] = self.restaurant.restaurant_name if self.restaurant else None
        result['payment_type'] = self.payment_type if self.payment_type else None
        result['payment_date'] = self.payment_date if self.payment_date else None
        result['start_date'] = self.start_date if self.start_date else None
        result['end_date'] = self.end_date if self.end_date else None
        result['customer_amount'] = self.customer_amount if self.customer_amount else None

        print result
        return result

class Coupon(models.Model):
    customer = models.ForeignKey('Customer', null=True)
    coupon_type = models.CharField(max_length=100)
    coupon_no = models.IntegerField(null=True)
    coupon_date = models.DateField()
    is_valid = models.BooleanField(default = False)

    def __unicode__(self):
        return "{} {} {} {}".format(self.id, self.coupon_type, self.coupon_no, self.coupon_date, self.is_valid)

    def get_json(self):
        result = {}
        result['id'] = self.id if self.id else None
        result['customer_id'] = self.customer.id if self.customer else None
        result['customer_fname'] = self.customer.customer_fname if self.customer else None
        result['coupon_type'] = self.coupon_type if self.coupon_type else None
        result['coupon_no'] = self.coupon_no if self.coupon_no else None
        result['coupon_date'] = self.coupon_date if self.coupon_date else None
        result['is_valid'] = self.is_valid if self.is_valid else None

        #print result
        return result


class Restaurant(models.Model):
    admin = models.OneToOneField(User, null=True)
    restaurant_name = models.CharField(max_length=300)
    restaurant_address = models.CharField(max_length=300)
    restaurant_contact = models.IntegerField()
    restaurant_opening_time = models.TimeField()
    restaurant_closing_time = models.TimeField()
    

    def __unicode__(self):
        return "{} {} {} {} {}".format(self.id, self.restaurant_name, self.restaurant_address,
                                       self.restaurant_contact, self.restaurant_opening_time,
                                       self.restaurant_closing_time
                                      )

    def get_json(self):
        result = {}
        result['id'] = self.id if self.id else None
        result['admin_id'] = self.admin.id if self.admin else None
        result['first_name'] = self.admin.first_name if self.admin else None
        result['last_name'] = self.admin.last_name if self.admin else None
        result['restaurant_name'] = self.restaurant_name if self.restaurant_name else None
        result['restaurant_address'] = self.restaurant_address if self.restaurant_address else None
        result['restaurant_contact'] = self.restaurant_contact if self.restaurant_contact else None
        result['restaurant_opening_time'] = str(self.restaurant_opening_time) if self.restaurant_opening_time else None
        result['restaurant_closing_time'] = str(self.restaurant_closing_time) if self.restaurant_closing_time else None

        print result
        return result

class Restaurantleave(models.Model):
    restaurant_off_date = models.DateField()
    leave_reason = models.CharField(max_length=2000)

    def __unicode__(self):
        return "{}".format(self.id, self.restaurant_off_date, self.leave_reason)

    def get_json(self):
        result = {}
        result['id'] = self.id if self.id else None
        result['restaurant_off_date'] = self.restaurant_off_date if self.restaurant_off_date else None
        result['leave_reason'] = self.leave_reason if self.leave_reason else None

        print result
        return result

