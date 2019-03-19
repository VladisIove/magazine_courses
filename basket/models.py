from django.db import models


from courses.models import Course
# Create your models here.


class CartItem(models.Model):
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	item_total = models.DecimalField(max_digits = 9, decimal_places=2, default=0.00)

	def __str__(self):
		return str(self.id)


class Cart(models.Model):
	items = models.ManyToManyField(CartItem, blank = True)
	cart_total = models.DecimalField(max_digits = 9, decimal_places=2, default=0.00)

	def __str__(self):
		return str(self.id)

	def add_to_cart(self, course_slug):
		cart = self
		course = Course.objects.get(slug = course_slug)
		course_add_to_cart, _ = CartItem.objects.get_or_create(course = course, item_total = course.price)
		if course_add_to_cart not in cart.items.all():
			cart.items.add(course_add_to_cart)
			cart.save()

	def remove_from_cart(self, course_slug):
		cart = self
		course = Course.objects.get(slug = course_slug)
		for cart_item in cart.items.all():
			if cart_item.course == course:
				cart.items.remove(cart_item)
				cart.save()



