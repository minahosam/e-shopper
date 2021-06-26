from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class index(models.Model):
    product_name=models.CharField(max_length=20)
    product_price=models.FloatField(default=0)
    add_to_cart=models.ManyToManyField(User,related_name='cart',blank=True,null=True)
    add_to_wishlist=models.ManyToManyField(User,related_name='wishlist',blank=True,null=True)  
    add_to_compare=models.ManyToManyField(User,related_name='compare',blank=True,null=True)
    product_photo=models.ImageField(upload_to='product_photo',default='')
    product_category=models.ForeignKey('category',related_name='cat',on_delete=models.CASCADE)
    product_brand=models.ForeignKey('brand',related_name='brand',on_delete=models.CASCADE)
    product_time_added=models.TimeField(auto_now=True)
    product_date_added=models.DateField(auto_now=True)
    slug=models.SlugField(default='')
    def __str__(self):
        return self.product_name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.product_name)
        super(index, self).save(*args, **kwargs) # Call the real save() method
class category(models.Model):
    category_name=models.CharField(max_length=10)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural='categories'
class brand(models.Model):
    brand_name=models.CharField(max_length=30)
    def __str__(self):
        return self.brand_name
class main_footer(models.Model):
    telephone_number=models.IntegerField(default=0)
    e_mail=models.EmailField(max_length=30)
    facebook_link=models.CharField(max_length=50)
    twitter_link=models.CharField(max_length=50)
    linkedin_link=models.CharField(max_length=50)
    google_link=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)