from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator 
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse


from .models import Course, LessonCourse
from .forms import HelpForm


from user_profile.models import User
from basket.models import Cart
# Create your views here.


class CourseBoughtView(ListView):
	context_object_name = 'courses'
	template_name = 'list_bought_courses.html'

	def get_queryset(self):
		user = User.objects.get(username=self.request.user)
		return user.courses.all()


class CourseListView(ListView):
	queryset = Course.objects.all()
	context_object_name = 'courses'
	template_name = "home.html"


	def get_context_data(self, **kwargs):
		context = super(CourseListView, self).get_context_data(**kwargs)
		try:
			cart_id = self.request.session['cart_id']
			cart = Cart.objects.get(id=cart_id)
			self.request.session['total'] = cart.items.count()
		except:
			cart = Cart()
			cart.save()
			cart_id = cart.id
			self.request.session['cart_id'] = cart_id
			cart = Cart.objects.get(id=cart_id)

		context['cart'] = cart	
		return context

class CourseDetailView(DetailView):
	model = Course
	template_name = "courseDetail.html"

	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		try:
			cart_id = self.request.session['cart_id']
			cart = Cart.objects.get(id=cart_id)
			self.request.session['total'] = cart.items.count()
		except:
			cart = Cart()
			cart.save()
			cart_id = cart.id
			self.request.session['cart_id'] = cart_id
			cart = Cart.objects.get(id=cart_id)

		context['cart'] = cart	
		return context

def viedoLessons(request, name_course):
	course = Course.objects.get(slug = name_course)
	lessons = LessonCourse.objects.all().filter(nameCourse=course.id)
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

	paginator = Paginator(lessons, 1)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''
	context = {
		'course': course,
		'lessons': lessons,
		'page_object': page,
		'cart': cart,
		'next_url': next_url,
		'prev_url': prev_url,
	}

	return render(request, 'videoCourse.html', context)

"""
class VideoLessonsListView(ListView):
	template_name = "lessoncourse_list.html"
	context_object_name = 'lessons'
	paginate_by = 1

	def get_queryset(self,name_course, *args, **kwargs):
		return LessonCourse.objects.get(nameCourse = name_course)

	def get_context_data(self, **kwargs):
		context = super(VideoLessonsListView, self).get_context_data(**kwargs)
		try:
			cart_id = self.request.session['cart_id']
			cart = Cart.objects.get(id=cart_id)
			self.request.session['total'] = cart.items.count()
		except:
			cart = Cart()
			cart.save()
			cart_id = cart.id
			self.request.session['cart_id'] = cart_id
			cart = Cart.objects.get(id=cart_id)
		context['cart'] = cart	
		return context


def get(self, request, name_course_slug):
		self.name_course_slug = name_course_slug
		name_course = Course.objects.get(slug = self.name_course_slug)
		print()
		print(name_course)
		print()
		lessons = LessonCourse.objects.get(nameCourse = name_course)
		context = {
			'name_course': name_course,
			'lessons': lessons
		}
		return render(request, 'viedoeCourse.html', context)"""



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
			message = 'Письмо отправлено'
			messages.success(request, message) 
			return render(request, 'help.html', {'form': form})
			#return HttpResponse('Письмо отправлено')	
	else:
		form = HelpForm()

	return render(request, 'help.html', {'form': form})




