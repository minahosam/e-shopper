from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from Profile.models import *
# Create your models here.
aviability=[('In Stock','In Stock'),('Out Of Stock','Out Of Stock')]
condition=[('New','New'),('Used','Used')]
class index(models.Model):
    product_name=models.CharField(max_length=20)
    product_price=models.FloatField(default=0)
    add_to_cart=models.ManyToManyField(User,related_name='cart',blank=True,null=True)
    add_to_wishlist=models.ManyToManyField(User,related_name='wishlist',blank=True,null=True)  
    add_to_compare=models.ManyToManyField(User,related_name='compare',blank=True,null=True)
    product_photo=models.ImageField(upload_to='product_photo',default=None)
    product_category=models.ForeignKey('category',related_name='cat',on_delete=models.CASCADE)
    product_brand=models.ForeignKey('brand',related_name='brand',on_delete=models.CASCADE)
    product_time_added=models.TimeField(auto_now=True)
    product_date_added=models.DateField(auto_now=True)
    transaction_code=models.CharField(max_length=10)
    product_aviability=models.CharField(max_length=17,choices=aviability,default='In Stock')
    product_condition = models.CharField(max_length=20,choices=condition,default='New')
    product_description=models.CharField(max_length=150,default='')
    product_quantity=models.IntegerField(default=0)
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
        return str(self.brand_name)
    # @staticmethod
    # def get_brand_by_id(brand_id):
    #     if brand_id:
    #         return brand.objects.filter(brand = brand_id)
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
class review(models.Model):
    review_content=models.TextField()
    review_author=models.ForeignKey(User,related_name='review_author', on_delete=models.CASCADE)
    review_time=models.TimeField(auto_now=True)
    review_date=models.DateField(auto_now=True)
    #rateing
    def __str__(self):
        return str(self.review_author)
class customer(models.Model):
    username=models.OneToOneField(User,related_name='customer_username', on_delete=models.CASCADE)
    e_mail=models.ForeignKey(userprofile,related_name='customer_email',to_field='email', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.username)
class order(models.Model):
    order_customer=models.ForeignKey(userprofile,related_name='order_customer', on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True)
    order_time=models.TimeField(auto_now_add=True)
    order_completed=models.BooleanField(default=False)
    transaction_id=models.CharField(default=0, max_length=50)
    def __str__(self):
        return str(self.order_customer)
class orderItem(models.Model):
    item_name=models.ForeignKey(index,related_name='item_name', on_delete=models.CASCADE)
    item_order=models.ForeignKey(order,related_name='item_order', on_delete=models.CASCADE)
    item_time_added=models.TimeField(auto_now_add=True)
    item_date_added=models.DateField(auto_now_add=True)
    item_quantity=models.IntegerField(default=1)
    @property
    def total_selected_item(self):
        total = self.item_name.product_price * self.item_quantity
        return total
    def __str__(self):
        return f'{self.item_name}-----------{self.item_quantity}'
class country(models.Model):
    country_name=models.CharField(max_length=20)
    def __str__(self):
        return self.country_name
    class Meta:
        verbose_name_plural = 'countries'
class state(models.Model):
    state_country=models.ForeignKey(country,related_name='state_country', on_delete=models.CASCADE)
    state_name=models.CharField(max_length=50)
    def __str__(self):
        return self.state_name