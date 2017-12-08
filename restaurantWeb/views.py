from restaurantWeb.models import Customer,Dish,Order,CustomerPaymentMapping,Coupon,Restaurant
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout
import json, datetime, calendar
from django.core.management.base import CommandError

def convert_date_to_epoch(date):
    return int(date.strftime('%s'))*1000 if date else None

def convert_epoch_to_date(epoch):
    return datetime.datetime.fromtimestamp(long(epoch)/1000.0) if epoch else None

def save_customer(request):
    json_obj = json.loads(request.body)

    input_restaurant_id = json_obj.get("restaurantId")
    input_username = json_obj.get("username")
    input_password = json_obj.get("password")
    input_first_name = json_obj.get("firstName")
    input_last_name = json_obj.get("lastName")
    input_confirm_password = json_obj.get("confirmPassword")
    input_customer_address = json_obj.get("customerAddress")
    input_customer_contact = json_obj.get("customerContact")

    if (not input_password) or (not input_confirm_password):
        return JsonResponse({"validation": "Please Enter a correct password", "status": False})

    if input_password != input_confirm_password:
        return JsonResponse({"validation": "Passwords does not matched", "status": False})

    user_obj = User.objects.create(username=input_username, first_name=input_first_name, 
                                   last_name=input_last_name)
    user_obj.set_password(input_password)
    user_obj.save()

    restaurant_obj = Restaurant.objects.get(id=input_restaurant_id)

    print input_customer_address, input_customer_contact

    if not input_customer_address:
        return JsonResponse({"validation": "Enter Customer Address ", "status": False})

# method for Customer
    customer_obj = Customer.objects.create(customer_address=input_customer_address,
                                           customer_contact=input_customer_contact,
                                           restaurant=restaurant_obj,
                                           user=user_obj
                                          )

    return JsonResponse({"validation": "Customer Info saved successfully", "status": True})


def customer_login(request):
    json_obj = json.loads(request.body)
    username = json_obj.get('username')
    password = json_obj.get('password')
    print json_obj 
    if not username:
        return JsonResponse({"validation": "Please enter a valid username..!!", "status": False})

    user = authenticate(username=username, password=password)

    if not user:
        print 'User not found in db'
        return JsonResponse({"validation": "Invlid User", "status": False})

    if not user.is_active:
        print 'user is inactive'
        return JsonResponse({"validation": "Invlid User", "status": False})

    login(request, user)

    return JsonResponse({"validation": "Login Successful", "status": True})


def customer_logout(self, request):
    logout(request)

    return JsonResponse({"validation": "logout Successful", "status": True})



def get_customer(request):
    json_obj=json.loads(request.body)
    customer_id = json_obj.get("customerId")

    customer_obj = Customer.objects.get(id=customer_id)

    customer_json_object = customer_obj.get_json()

    return JsonResponse({"data": customer_json_object, "status": True})

def get_all_customer(request):
    json_obj=json.loads(request.body)
    all_customer_list=[]
    customers_json_object = Customer.objects.all()
    for customer in customers:
        all_customer_list.append(customer.get_json())
    return JsonResponse({"data": all_customer_list, "status": True})


def search_customer(request):
    data_dict = json.loads(request.body)
    search_string = data_dict.get("searchString")

    all_customer_list = []

    customers = Customer.objects.filter(customer_fname__contains=search_string)

    for customer in customers:
        all_customer_list.append(customer.get_json())
            
    return JsonResponse({'data': all_customer_list, 'status': True})


#For Dish

def save_dish(request):
    # json_obj = json.loads(request.body)
    json_obj = request.POST

    print 'request.FILES: ', request.FILES

    input_restaurant_id = json_obj.get("restaurantId")
    input_dish_name = json_obj.get("dishName")
    input_dish_type = json_obj.get("dishType")
    input_dish_pic = request.FILES.get("dishPic")

    restaurant_obj = Restaurant.objects.get(id=input_restaurant_id)
    

    print input_dish_name, input_dish_type, input_dish_pic

    if not input_dish_name:
        return JsonResponse({"validation": "Enter Dish Name", "status": True})

    if not input_dish_type:
        return JsonResponse({"validation": "Enter Dish Type", "status": True})


# method for Dish
    dish_obj = Dish.objects.create(dish_name=input_dish_name,dish_type=input_dish_type,
                                   dish_pic=input_dish_pic,restaurant=restaurant_obj
                                  )
                                          

    return JsonResponse({"validation": "Dish Info saved successfully", "status": True})

def get_dish(request):
    json_obj=json.loads(request.body)
    dish_id = json_obj.get("dishId")

    dish_obj = Dish.objects.get(id=dish_id)

    dish_json_object = dish_obj.get_json()

    return JsonResponse({"data": dish_json_object, "status": True})

def get_all_dish(request):
    json_obj=json.loads(request.body)
    all_dish_list=[]
    dishes_json_object = Dish.objects.all()
    for dish in dishes:
        all_dish_list.append(dish.get_json())
    return JsonResponse({"data": all_dish_list, "status": True})


def search_dish(request):
    data_dict = json.loads(request.body)
    search_string = data_dict.get("searchString")

    all_dish_list = []

    dishes = Dish.objects.filter(dish_name__contains=search_string)

    for dish in dishes:
        all_dish_list.append(dish.get_json())
            
    return JsonResponse({'data': all_dish_list, 'status': True})


#For Order

def save_order(request):

    json_obj = json.loads(request.body)
    input_restaurant_id = json_obj.get("restaurantId")

    input_item_name = json_obj.get("itemName")
    input_item_no = json_obj.get("itemNo")
    input_order_address = json_obj.get("orderAddress")

    restaurant_obj = Restaurant.objects.get(id=input_restaurant_id)
    

    print input_item_name, input_item_no, input_order_address

    if not input_item_name:
        return JsonResponse({"validation": "Enter Item Name", "status": True})

    if not input_order_address:
        return JsonResponse({"validation": "Enter Order Address", "status": True})


# method for Order
    order_obj = Order.objects.create(item_name=input_item_name,item_no=input_item_no,
                                     order_address=input_order_address,
                                     restaurant=restaurant_obj
                                    )
                                          

    return JsonResponse({"validation": "Order Info saved successfully", "status": True})

def get_order(request):
    json_obj=json.loads(request.body)
    order_id = json_obj.get("orderId")

    order_obj = Order.objects.get(id=order_id)

    order_json_object = order_obj.get_json()

    return JsonResponse({"data": order_json_object, "status": True})

def get_all_order(request):
    json_obj=json.loads(request.body)
    all_order_list=[]
    orders_json_object = Order.objects.all()
    for order in orders:
        all_order_list.append(order.get_json())
    return JsonResponse({"data": all_order_list, "status": True})


def search_order(request):
    data_dict = json.loads(request.body)
    search_string = data_dict.get("searchString")

    all_order_list = []

    orders = Order.objects.filter(item_name__contains=search_string)

    for order in orders:
        all_order_list.append(order.get_json())
            
    return JsonResponse({'data': all_order_list, 'status': True})


#For Payment

def make_payment(request):
    json_obj = json.loads(request.body)
    input_restaurant_id = json_obj.get("restaurantId")
    input_payment_type = json_obj.get("paymentType")
    input_customer_id = json_obj.get("customerId")
    input_payment_date = json_obj.get("paymentDate")
    input_start_date = json_obj.get("startDate")
    input_end_date = json_obj.get("endDate")
    input_customer_amount = json_obj.get("customerAmount")

    customer_obj = Customer.objects.get(id=input_customer_id)
    restaurant_obj = Restaurant.objects.get(id=input_restaurant_id)
    

    print input_payment_type, input_payment_date, input_start_date, input_end_date, input_customer_amount

    if not input_payment_type:
        return JsonResponse({"validation": "Enter Payment Type", "status": True})


# method for Payment
    customer_payment_mapping_obj = CustomerPaymentMapping.objects.create(payment_type=input_payment_type,
                                         payment_date=input_payment_date,
                                         start_date=input_start_date,
                                         end_date=input_end_date,
                                         customer_amount=input_customer_amount,
                                         customer=customer_obj,
                                         restaurant=restaurant_obj
                                        )
                                          
    status = create_coupons(customer_payment_mapping_obj.start_date, customer_payment_mapping_obj.end_date, customer_obj)

    return JsonResponse({"validation": "Payment Info saved successfully", "status": True})

def get_payment(request):
    json_obj=json.loads(request.body)
    payment_id = json_obj.get("paymentId")

    payment_obj = Payment.objects.get(id=payment_id)

    payment_json_object = payment_obj.get_json()

    return JsonResponse({"data": payment_json_object, "status": True})

def get_all_payment(request):
    json_obj=json.loads(request.body)
    all_payment_list=[]
    payments_json_object = Payment.objects.all()
    for payment in payments:
        all_payment_list.append(payment.get_json())
    return JsonResponse({"data": all_payment_list, "status": True})


def search_payment(request):
    data_dict = json.loads(request.body)
    search_string = data_dict.get("searchString")

    all_payment_list = []

    payments = Payment.objects.filter(payment_type__contains=search_string)

    for payment in payments:
        all_payment_list.append(payment.get_json())
            
    return JsonResponse({'data': all_payment_list, 'status': True})


#For Coupon

def save_coupon(request):
    json_obj = json.loads(request.body)

    input_coupon_type = json_obj.get("couponType")
    input_customer_id = json_obj.get("customerId")
    input_coupon_no = json_obj.get("couponNo")
    input_coupon_date = json_obj.get("couponDate")
    input_is_valid = json_obj.get("isValid")

    customer_obj = Customer.objects.get(id=input_customer_id)

    coupon_date = convert_epoch_to_date(input_coupon_date)

    print 'coupon_date: ', coupon_date.date()

    if Coupon.objects.filter(customer=customer_obj, coupon_date=coupon_date.date()).count() >= 3:
        print 'Daily coupon limit exceed'
        return JsonResponse({"validation": "Coupon limit exceed", "status": False})
            
    print input_coupon_type, input_coupon_no, input_coupon_date

    if not input_coupon_type:
        return JsonResponse({"validation": "Enter Coupon Type", "status": False})


# method for Coupon
    coupon_obj = Coupon.objects.create(coupon_type=input_coupon_type,
                                       coupon_no=input_coupon_no,
                                       coupon_date=coupon_date.date(),
                                       customer=customer_obj,
                                       is_valid=input_is_valid
                                      )
                                    
    return JsonResponse({"validation": "Coupon Info saved successfully", "status": True})


def delete_coupon(request):
    first_day, last_day = get_date_range()

    print 'first_day: ', first_day
    print 'last_day: ', last_day

    coupons = Coupon.objects.filter(coupon_date__range=(first_day, last_day)).delete()

    return JsonResponse({"validation": "invalid coupons removed", "status": True})


def get_coupon(request):
    json_obj=json.loads(request.body)
    coupon_id = json_obj.get("couponId")

    coupon_obj = Coupon.objects.get(id=coupon_id)

    coupon_json_object = coupon_obj.get_json()

    return JsonResponse({"data": coupon_json_object, "status": True})


def scan_card(request):
    json_obj=json.loads(request.body)
    input_customer_id = json_obj.get("customerId")
    customer_obj = Customer.objects.get(id=input_customer_id)
    coupon_date = datetime.date.today()
    #coupon_date = convert_epoch_to_date(input_coupon_date)

    print 'coupon_date: ', coupon_date

    coupons = Coupon.objects.filter(customer=customer_obj, coupon_date=coupon_date, is_valid=True)

    if coupons.count() <= 0:
        return JsonResponse({"validation": "Coupon are not available for you", "status": False})

    coupon = coupons[0]

    coupon.is_valid = False
    coupon.save()

    return JsonResponse({"validation": "Daily Coupon scan", "status": True})
     


def get_all_coupon(request):
    json_obj=json.loads(request.body)
    all_coupon_list=[]
    coupons_json_object = Coupon.objects.all()
    for coupon in coupons:
        all_coupon_list.append(coupon.get_json())
    return JsonResponse({"data": all_coupon_list, "status": True})


def search_coupon(request):
    data_dict = json.loads(request.body)
    search_string = data_dict.get("searchString")

    all_coupon_list = []

    coupons = Coupon.objects.filter(coupon_type__contains=search_string)

    for coupon in coupons:
        all_coupon_list.append(coupon.get_json())
            
    return JsonResponse({'data': all_coupon_list, 'status': True})


def save_restaurant(request):

    json_obj = json.loads(request.body)

    input_restaurant_name = json_obj.get("restaurantName")
    input_username = json_obj.get("username")
    input_password = json_obj.get("password")
    input_first_name = json_obj.get("firstName")
    input_last_name = json_obj.get("lastName")
    input_confirm_password = json_obj.get("confirmPassword")
    input_restaurant_address = json_obj.get("restaurantAddress")
    input_restaurant_contact = json_obj.get("restaurantContact")
    input_restaurant_opening_time = json_obj.get("restaurantOpeningTime")
    input_restaurant_closing_time = json_obj.get("restaurantClosingTime")


    if (not input_password) or (not input_confirm_password):
        return JsonResponse({"validation": "Please Enter a correct password", "status": False})

    if input_password != input_confirm_password:
        return JsonResponse({"validation": "Passwords does not matched", "status": False})

    admin_obj = User.objects.create(username=input_username, first_name=input_first_name, 
                                   last_name=input_last_name)
    admin_obj.set_password(input_password)
    admin_obj.save()
    

    print input_restaurant_name, input_restaurant_address, input_restaurant_contact, input_restaurant_opening_time, input_restaurant_closing_time

    if not input_restaurant_name:
        return JsonResponse({"validation": "Enter Restaurant Name", "status": True})

    if not input_restaurant_address:
        return JsonResponse({"validation": "Enter Restaurant Address", "status": True})


# method for Restaurant
    restaurant_obj = Restaurant.objects.create(restaurant_name=input_restaurant_name,
                                               restaurant_address=input_restaurant_address, 
                                               restaurant_contact=input_restaurant_contact,
                                               restaurant_opening_time=input_restaurant_opening_time,
                                               restaurant_closing_time=input_restaurant_closing_time,
                                               admin=admin_obj
                                              )

    return JsonResponse({"validation": "Restaurant Info saved successfully", "status": True})


def admin_login(request):
    json_obj = json.loads(request.body)
    username = json_obj.get('username')
    password = json_obj.get('password')
    print json_obj 
    if not username:
        return JsonResponse({"validation": "Please enter a valid username..!!", "status": False})

    admin = authenticate(username=username, password=password)

    if not admin:
        print 'Admin not found in db'
        return JsonResponse({"validation": "Invlid Admin", "status": False})

    if not admin.is_active:
        print 'admin is inactive'
        return JsonResponse({"validation": "Invlid Admin", "status": False})

    login(request, admin)

    return JsonResponse({"validation": "Login Successful", "status": True})



def get_restaurant(request):
    json_obj=json.loads(request.body)
    restaurant_id = json_obj.get("restaurantId")

    restaurant_obj = Restaurant.objects.get(id=restaurant_id)

    restaurant_json_object = restaurant_obj.get_json()

    return JsonResponse({"data": restaurant_json_object, "status": True})


def get_all_restaurant(request):
    json_obj=json.loads(request.body)
    all_restaurant_list=[]
    restaurants_json_object = Restaurant.objects.all()
    for restaurant in restaurants:
        all_restaurant_list.append(restaurant.get_json())
    return JsonResponse({"data": all_restaurant_list, "status": True})


def search_restaurant(request):
    data_dict = json.loads(request.body)
    search_string = data_dict.get("searchString")

    all_restaurant_list = []

    restaurants = Restaurant.objects.filter(restaurant_name__contains=search_string)

    for restaurant in restaurants:
        all_restaurant_list.append(restaurant.get_json())
            
    return JsonResponse({'data': all_restaurant_list, 'status': True})


def create_coupons(start_date, end_date, customer_obj):
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    print start_date, end_date
    print type(start_date), type(end_date)
    
    day_count = end_date - start_date
    date = start_date
    for day in range(day_count.days):
        coupon1 = Coupon.objects.create(coupon_date=date, customer=customer_obj, is_valid=True, coupon_type='MONTHLY')
        coupon2 = Coupon.objects.create(coupon_date=date, customer=customer_obj, is_valid=True, coupon_type='MONTHLY')

        date = date + datetime.timedelta(days=1)

    return True


def get_date_range():
    today = datetime.datetime.today()
    
    previous_month = today.month - 1 if today.month - 1 != 0 else 12

    year = today.year

    if previous_month == 12:
        year = today.year - 1

    month_date_range = calendar.monthrange(year, previous_month)

    last_day_date = month_date_range[1]

    first_day = datetime.date(year, previous_month, 1)
    last_day = datetime.date(year, previous_month, last_day_date)

    return first_day, last_day




def save_restaurantleave(request):
    json_obj = json.loads(request.body)

    input_restaurant_off_date = json_obj.get("restaurantOffDate")
    input_leave_reason = json_obj.get("leaveReason")

    restaurant_leave_obj = Restaurantleave.objects.create(restaurant_off_date=input_restaurant_off_date,
                                                          leave_reason=input_leave_reason
                                                         )
                                    
    return JsonResponse({"validation": "Restaurantleave Info saved successfully", "status": True})


def get_restaurantleave(request):
    json_obj=json.loads(request.body)
    restaurantleave_id = json_obj.get("restaurantleaveId")

    restaurantleave_obj = Restaurantleave.objects.get(id=restaurantleave_id)

    restaurantleave_json_object = restaurantleave_obj.get_json()

    return JsonResponse({"data": restaurantleave_json_object, "status": True})


def get_all_restaurantleave(request):
    json_obj=json.loads(request.body)
    all_restaurantleave_list=[]
    restaurantleaves_json_object = Restaurantleave.objects.all()
    for restaurantleave in restaurantleaves:
        all_restaurantleave_list.append(restaurantleave.get_json())
    return JsonResponse({"data": all_restaurantleave_list, "status": True})


def search_restaurantleave(request):
    data_dict = json.loads(request.body)
    search_string = data_dict.get("searchString")

    all_restaurantleave_list = []

    restaurantleaves = Restaurantleave.objects.filter(leave_reason__contains=search_string)

    for restaurantleave in restaurantleaves:
        all_restaurantleave_list.append(restaurantleave.get_json())
            
            
    return JsonResponse({'data': all_restaurantleave_list, 'status': True})