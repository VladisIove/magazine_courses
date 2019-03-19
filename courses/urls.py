from django.urls import path
from django.views.generic import TemplateView


from .views import CourseList, CourseDetail, help_message

app_name = 'courses'

urlpatterns = [
	path('', CourseList, name='home_page'),
	path('help/', help_message, name = 'help'),
	path('about/', TemplateView.as_view( template_name ='about.html'), name = 'about'),
	path('faq/', TemplateView.as_view( template_name ='faq.html'), name = 'faq'),
	path('detail/<slug:slug>', CourseDetail, name='course_detail' )
]