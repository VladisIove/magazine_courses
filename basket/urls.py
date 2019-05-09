from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
	path('cart/', views.cart_view, name = 'cart'),
	path('add_to_cart/', views.add_to_cart_view, name='add_to_cart'),
	path('remove_from_cart/', views.remove_from_cart_view, name='remove_from_cart'),
	path('checkout/', views.checkout_view, name = 'checkout'),
	path('bought_course/', views.bought_courses_view, name = 'bought_course'),
]