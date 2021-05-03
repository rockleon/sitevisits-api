from django.contrib import admin
from .models import Account

class AdminAccount(admin.ModelAdmin):
    model = Account
    list_display = ('title', 'visits', 'key', 'url')


admin.site.register(Account, AdminAccount)
