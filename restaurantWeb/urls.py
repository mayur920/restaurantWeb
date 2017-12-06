"""restaurantWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from restaurantWeb.views import save_customer, customer_login, customer_logout, get_customer, get_all_customer, search_customer,\
                                save_dish, get_dish, get_all_dish, search_dish,\
                                save_order, get_order, get_all_order, search_order,\
                                make_payment, get_payment, get_all_payment, search_payment,\
                                save_coupon, delete_coupon, get_coupon, get_all_coupon, search_coupon, scan_card,\
                                save_restaurant, admin_login,get_restaurant, get_all_restaurant, search_restaurant
                                



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^save/customer/$', save_customer),
    url(r'^get/customer/$', get_customer),
    url(r'^get/all/customer/$', get_all_customer),
    url(r'^search/customer/$', search_customer),
    url(r'^save/dish/$', save_dish),
    url(r'^get/dish/$', get_dish),
    url(r'^get/all/dish/$', get_all_dish),
    url(r'^search/dish/$', search_dish),
    url(r'^save/order/$', save_order),
    url(r'^get/order/$', get_order),
    url(r'^get/all/order/$', get_all_order),
    url(r'^search/order/$', search_order),
    url(r'^make/payment/$', make_payment),
    url(r'^get/payment/$', get_payment),
    url(r'^get/all/payment/$', get_all_payment),
    url(r'^search/payment/$', search_payment),
    url(r'^save/coupon/$', save_coupon),
    url(r'^delete/coupon/$', delete_coupon),
    url(r'^get/coupon/$', get_coupon),
    url(r'^get/all/coupon/$', get_all_coupon),
    url(r'^search/coupon/$', search_coupon),
    url(r'^scan/card/$', scan_card),
    url(r'^save/restaurant/$', save_restaurant),
    url(r'^get/restaurant/$', get_restaurant),
    url(r'^get/all/restaurant/$', get_all_restaurant),
    url(r'^search/restaurant/$', search_restaurant),
    url(r'^customer/login/$', customer_login),
    url(r'^customer/logout/$', customer_logout),
    url(r'^admin/login/$', admin_login)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
