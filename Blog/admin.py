from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','post_creator','post_date','post_status')
    list_filter=('post_creator','post_date')
    search_fields=('post_creator',)
    list_editable=('post_status',)
    date_hierarchy=('post_date')
admin.site.register(blog,PostAdmin)
admin.site.register(comment)