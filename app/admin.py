
from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('id', 'username', 'email')
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
