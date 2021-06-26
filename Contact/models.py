from django.db import models

# Create your models here.
class contact_info(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=200 )
    subject=models.CharField(max_length=300)
    message=models.TextField()
    def __str__(self):
        return self.name