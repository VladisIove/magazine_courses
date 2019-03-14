from django.db import models
from django.urls import reverse
# Create your models here.

class Course( models.Model ):
	name = models.CharField( max_length=200, blank=False, null=False, db_index=True, unique=True, verbose_name='Название курса')
	slug = models.SlugField( max_length=200, blank=False, null=False, db_index=True, unique=True)
	image = models.ImageField(upload_to = 'img/course_logo/', blank=False, null=False, verbose_name = 'Фото курса')
	little_description = models.CharField( max_length=200, verbose_name='Небольшое описание курса на главной странице')
	description = models.TextField(blank=False, null=False, verbose_name='Полное описание курса')
	price = models.DecimalField( max_digits=10, decimal_places=2)


	week_one = models.CharField( max_length=200, blank=False, null=False, verbose_name='Название первой недели')
	description_week_one = models.TextField( blank=False, null=False, verbose_name='Описание первой недели')

	week_second = models.CharField( max_length=200, blank=False, null=False, verbose_name='Название второй недели')
	description_week_second = models.TextField( blank=False, null=False, verbose_name='Описание второй недели')

	week_third = models.CharField( max_length=200, blank=False, null=False, verbose_name='Название третьей недели')
	description_week_third = models.TextField( blank=False, null=False, verbose_name='Описание третьей недели')

	week_fourth = models.CharField( max_length=200, blank=False, null=False, verbose_name='Название четвертой недели')
	description_week_fourth = models.TextField( blank=False, null=False, verbose_name='Описание четвертой недели')

	created = models.DateTimeField( auto_now_add=True )

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('courses:course_detail', args = [self.slug])

	class Meta:
		ordering = ['-created']


class LessonCourse( models.Model ):
	nameCourse = models.ForeignKey(Course, related_name = 'lesson_course', verbose_name='Курс', on_delete = models.CASCADE)
	nameDay = models.CharField( max_length=200, blank=False,null=False, db_index=True, verbose_name='Название урока')
	slug = models.SlugField( max_length=200, db_index=True)
	description = models.TextField(verbose_name='Описание Урока')
	url_video = models.URLField(max_length=200)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('courses:CourseLesson', args = [self.slug])

