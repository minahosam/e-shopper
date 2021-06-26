from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=50)
    tags=TaggableManager()
    post_time=models.TimeField(auto_now=True)
    post_date=models.DateField(auto_now=True)
    post_image=models.ImageField(default='',upload_to='post_image/')
    post_status=models.BooleanField(default=False)
    post_creator=models.ForeignKey(User,related_name='creator',on_delete=models.SET_NULL,null=True)
    post_content=models.TextField(max_length=500)
    liked_post=models.ManyToManyField(User,related_name='liked')
    disliked_post=models.ManyToManyField(User,related_name='disliked')
    #avg_rating
    def __str__(self):
        return str(self.post_creator)
    class Meta:
        ordering=['id']
class comment(models.Model):
    comment_author=models.ForeignKey(User,related_name='comment_author',on_delete=models.SET_NULL,null=True)
    author_email=models.EmailField(max_length=100)
    comment_reply=models.ForeignKey("self", related_name='c_replied', on_delete=models.CASCADE,null=True)
    current_city=models.CharField(max_length=50)
    comment_content=models.TextField(max_length=300)
    comment_blog=models.ForeignKey(blog,related_name='comment',on_delete=models.CASCADE)
    comment_time=models.TimeField(auto_now=True)
    comment_date=models.DateField(auto_now=True)
    def __str__(self):
        return str(self.comment_author)
    class Meta:
        ordering=['comment_blog']