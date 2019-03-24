from django.urls import path
from django.views.generic import TemplateView


from .views import CourseListView, CourseDetailView, help_message, viedoLessons

app_name = 'courses'

urlpatterns = [
	path('', CourseListView.as_view(), name='home_page'),
	path('help/', help_message, name = 'help'),
	path('about/', TemplateView.as_view( template_name ='about.html'), name = 'about'),
	path('faq/', TemplateView.as_view( template_name ='faq.html'), name = 'faq'),
	path('detail/<slug:slug>', CourseDetailView.as_view(), name='course_detail' ),
	path('course/<slug:name_course>lessons/', viedoLessons, name='videoLessonsCourse' ),
]