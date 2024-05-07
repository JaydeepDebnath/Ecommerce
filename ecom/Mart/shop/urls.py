from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path("index/",views.index,name = "ShopHome"),
    path("about/",views.about,name = "Aboutus"),
    path("contact/",views.contact,name = "Contactus"),
    path("tracker/",views.tracker,name = "Trackingstatus"),
    path("search/",views.search,name = "search"),
    path("productview/",views.productview,name = "Product"),
    path("checkout/",views.checkout,name = "checkout"),
]