from django.contrib import admin
from .models import *
# Register your models here.
class  product_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}
admin.site.register(main_footer)
admin.site.register(index,product_admin)
admin.site.register(category)
admin.site.register(brand)
admin.site.register(order)
admin.site.register(orderItem)
admin.site.register(customer)
admin.site.register(country)
admin.site.register(state)