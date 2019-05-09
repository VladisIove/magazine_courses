from django.db import models
from django.contrib.auth.models import AbstractUser

from courses.models import Course
# Create your models here.

class User(AbstractUser):
	courses = models.ManyToManyField(Course, blank = True, null=True)

	def add_course(self, course_id):
		user = self
		course = Course.objects.get(id = str(course_id))
		user.courses.add(course)
		user.save()


	def bought_courses(self):
		user = self 
		c = []
		for course in  user.courses.all():
			c.append(course.name)
		return c