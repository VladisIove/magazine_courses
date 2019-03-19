from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 

from courses.models import Course
from .models import Cart , CartItem


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


	context = {
		'cart': cart,
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
	return JsonResponse({'cart_total': cart.items.count()})


def remove_from_cart_view(request):
	course = Course.objects.get(slug = course_slug)
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
	cart.remove_from_cart(course.slug)
	return JsonResponse({'cart_total': cart.items.count()})
	
 