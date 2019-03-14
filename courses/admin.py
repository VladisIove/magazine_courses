from django.contrib import admin
from .models import Course
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




admin.site.register(Course,CourseAdmin)
	
