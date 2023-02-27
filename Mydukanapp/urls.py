from.import views
from django.urls import path



urlpatterns = [
    path('', views.Homepage, name="Homepage"),
    path('Productdetails/<str:id>/', views.Productdetails, name="Productdetails"),
    path('Cartpage/', views.Cartpage, name="Cartpage"),
    path('Checkout/', views.Checkout, name="Checkout"),
    path('Statuspage/', views.Statuspage, name="Statuspage"),
    path('Payment/', views.Payment, name="Payment"),

    path('Loginpage/', views.Loginpage, name="Loginpage"),
    path('Logout/', views.Logout, name="Logout"),
    path('Registrationpage/', views.Registrationpage, name="Registrationpage"),
]