from django.contrib import admin
from .models import Course, LessonCourse
# Register your models here.

class CourseAdmin( admin.ModelAdmin ):
	list_display = ['name',
									'slug',
									'little_description',
									'price',
									]
	list_display_links = ('name', )
	prepopulated_fields = {'slug': ('name',)}
	list_editable = ['price', 'little_description']

class LessonCourseAdmin( admin.ModelAdmin ):
	list_display = ['nameDay', 
									'nameCourse', 
									'slug', 
									'url_video']
	list_display_links = ['nameDay',]
	prepopulated_fields = {'slug': ('nameDay', )}
	list_editeble = ['nameDay','nameCourse','price']



admin.site.register(Course,CourseAdmin)
admin.site.register(LessonCourse, LessonCourseAdmin)
	
