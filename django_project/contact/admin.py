from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_no')
    search_fields = ('name', 'phone_no')#enable searchby name and phone no
    
admin.site.register(Contact,ContactAdmin)