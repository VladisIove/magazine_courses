

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 

from courses.models import Course
from .models import Cart , CartItem

from user_profile.models import User
# Create your views here.

def cart_view( request ):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(slug=course_slug)

	new_cart_total = 0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()
	context = {
		'cart': cart,
		'cart_total_price': cart.cart_total,
	}
	return render(request, 'cart.html', context=context)

def add_to_cart_view(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(slug=course_slug)
		
	course_slug = request.GET.get('course_slug')
	course = Course.objects.get(slug = course_slug)
	cart.add_to_cart(course.slug)
	new_cart_total = 0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()
	return JsonResponse({'cart_total': cart.items.count(), 'cart_total_price': cart.cart_total})


def remove_from_cart_view(request):

	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(slug=course_slug)
	course_slug = request.GET.get('course_slug')
	course = Course.objects.get(slug = course_slug)
	cart.remove_from_cart(course.slug)
	new_cart_total = 0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()
	return JsonResponse({'cart_total': cart.items.count(), 'cart_total_price': cart.cart_total})
	
def checkout_view(request):
 	try:
 		cart_id = request.session['cart_id']
 		cart = Cart.objects.get(id=cart_id)
 		request.session['total'] = cart.items.count()
 	except:
 		cart = Cart()
 		cart.save()
 		cart_id = cart.id
 		request.session['cart_id'] = cart_id
 		cart = Cart.objects.get(slug=course_slug)

 	context = {
 		'cart': cart,
 		}

 	return render(request, 'checkout.html', context)


def bought_courses_view(request):

	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(slug=course_slug)

	user = User.objects.get(id = request.user.id )
	for course_id in cart.items.all() :
		user.add_course(course_id)
		course = Course.objects.get(id = str(course_id))
		cart.remove_from_cart(course.slug)

	courses = Course.objects.all()
	context = {
		'courses': courses,
	}
	return render(request, 'home.html', context)

