from django.contrib import admin

# Register your models here.
from .models import Reviews,Userr,Project


admin.site.register(Reviews)
admin.site.register(Userr)
admin.site.register(Project)
