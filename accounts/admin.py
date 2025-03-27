from django.contrib import admin
from .models import User  # Import the User model

# Register your models here.


admin.site.site_header = "NewChat Admin"
admin.site.site_title = "NewChat Admin Portal"
admin.site.index_title = "Welcome to NewChat Portal"

admin.site.register(User)
