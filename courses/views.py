from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import EmailMessage

from .models import Course
from .forms import HelpForm
# Create your views here.


class CourseListView(ListView):
  model = Course
  template_name = "home.html"
  context_object_name = 'courses'

class CourseDetailView(DetailView):
	model = Course
	template_name = "courseDetail.html"
	context_object_name = 'course'


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




