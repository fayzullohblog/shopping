from django.contrib import admin

from accountapp.models import ProfileModel, UserModel, UserTypeModel

# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(UserTypeModel)
admin.site.register(UserModel)


