from django.contrib import admin
from loginaudit.models import UserAuthAction


class UserAuthActionAdmin(admin.ModelAdmin):
    list_display = ('action_type', 'user', 'performed')
    list_filter = ('user', 'performed')

    def __init__(self, *args, **kwargs):
        super(UserAuthActionAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )


admin.site.register(UserAuthAction, UserAuthActionAdmin)
