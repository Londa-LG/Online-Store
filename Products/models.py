from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    faq_title = models.CharField(max_length=100,default="FAQ")
    faq = models.TextField()

class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()

class Product(models.Model):
    title = models.CharField(max_length=100)
    pic = models.ImageField(default='default.jpg',upload_to= 'product_pics')
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    in_stock = models.DecimalField(max_digits=100,decimal_places=0)

    def get_absolute_url(self):
        return f"/products/{self.id}"

