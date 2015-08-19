from django.contrib import admin
from loginaudit.models import UserAuthAction


class UserAuthActionAdmin(admin.ModelAdmin):
    fields = ('action_type', 'user', 'created')

admin.site.register(UserAuthAction, UserAuthActionAdmin)
