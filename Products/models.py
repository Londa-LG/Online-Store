from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    faq_title = models.CharField(max_length=100,default="FAQ")
    faq = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    pic = models.ImageField(default='default.jpg',upload_to= 'product_pics')
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    in_stock = models.DecimalField(max_digits=100,decimal_places=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}"

