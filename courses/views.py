from django.shortcuts import render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import EmailMessage

from .models import Course
from .forms import HelpForm

from basket.models import Cart
# Create your views here.


def CourseList(request):
	courses = Course.objects.all()
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)

	context = {
		'courses':courses,
		'cart': cart,
	}
	return render(request, 'home.html', context)

def CourseDetail(request,slug):
	course = get_object_or_404(Course,slug=slug)
	
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)


	context = {
		'course':course, 
		'cart':cart,
	}
	return render(request, 'courseDetail.html', context)




def help_message(request):
	if request.method == 'POST':
		form = HelpForm( request.POST )

		if form.is_valid():
			current_site = get_current_site(request)
			mail_subject = 'Пришло письмо с поддержки'
			message = request.POST.get('email') + ' ' + request.POST.get('name') +' '+ request.POST.get('message')
			to_email = 'vlad.shelemakha0302@gmail.com'
			email = EmailMessage( mail_subject, message, to = [to_email] )
			email.send()		
			return HttpResponse('Письмо отправлено')	
	else:
		form = HelpForm()

	return render(request, 'help.html', {'form': form})




