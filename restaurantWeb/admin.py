from django.contrib import admin
from restaurantWeb.models import Customer,Dish,Order,CustomerPaymentMapping,Coupon,Restaurant,Restaurantleave



class CustomerAdmin(admin.ModelAdmin):
	list_display = ('customer_address', 'customer_contact', 'restaurant', 'user')
	list_filter = ('customer_address', 'customer_contact', 'restaurant', 'user')
	search_fields = ('customer_address', 'user__first_name')

admin.site.register(Customer, CustomerAdmin)

#-----------------------------------------------------------------------------------------------------

class DishAdmin(admin.ModelAdmin):
	list_display = ('dish_name', 'dish_type', 'restaurant')
	list_filter = ('dish_type', 'dish_name', 'restaurant')
	search_fields = ('dish_name', 'dish_type')

admin.site.register(Dish, DishAdmin)

#-----------------------------------------------------------------------------------------------------

class OrderAdmin(admin.ModelAdmin):
	list_display = ('item_name', 'item_no', 'order_address', 'restaurant')
	list_filter = ('item_no', 'item_name', 'order_address', 'restaurant')
	search_fields = ('item_no', 'order_address')

admin.site.register(Order, OrderAdmin)

#----------------------------------------------------------------------------------------------------

class CustomerPaymentMappingAdmin(admin.ModelAdmin):
	list_display = ('payment_type', 'payment_date', 'start_date', 'end_date', 'customer_amount', 'customer', 'restaurant')
	list_filter = ('payment_date', 'payment_type', 'start_date', 'end_date', 'customer_amount', 'customer', 'restaurant')
	search_fields = ('payment_type', 'payment_date')

admin.site.register(CustomerPaymentMapping, CustomerPaymentMappingAdmin)

#----------------------------------------------------------------------------------------------------

class CouponAdmin(admin.ModelAdmin):
	list_display = ('coupon_type', 'coupon_no', 'coupon_date', 'customer', 'is_valid')
	list_filter = ('coupon_no', 'coupon_date', 'coupon_type', 'customer', 'is_valid')
	search_fields = ('coupon_no', 'coupon_type')

admin.site.register(Coupon, CouponAdmin)

#----------------------------------------------------------------------------------------------------

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('restaurant_name', 'restaurant_address', 'restaurant_contact', 
					'restaurant_opening_time', 'restaurant_closing_time', 'admin')

	list_filter = ('restaurant_address', 'restaurant_name', 'restaurant_contact',)

	search_fields = ('restaurant_address', 'restaurant_name')

admin.site.register(Restaurant, RestaurantAdmin)

#----------------------------------------------------------------------------------------------------
class RestaurantleaveAdmin(admin.ModelAdmin):
	list_display = ('restaurant_off_date',  'leave_reason')

	list_filter = ('restaurant_off_date', 'leave_reason')

	search_fields = ('restaurant_off_date', 'leave_reason')

admin.site.register(Restaurantleave, RestaurantleaveAdmin)

#-----------------------------------------------------------------------------------------------------