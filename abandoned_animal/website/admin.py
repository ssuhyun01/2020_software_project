from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import SignupForm, ChangeForm

from .models import User, Post, Comment, Shelter, ShelterInformation, Message

# Register your models here.
class ProjectUserAdmin(UserAdmin):
    # 회원 업데이트 폼 연결
    form = ChangeForm
    list_display = ('username', 'phone')
    list_filter = ('is_activate', 'is_superuser')
    fieldsets = (
        ('아이디', {'fields': ('username', 'password')}),
        ('개인 정보', {'fields': ('phone')}),
        ('권한', {'fields': ('is_superuser',)}),
    )

    # 회원 추가 폼 연결
    add_form = SignupForm
    add_fieldsets = (
        ('기본 정보', {'fields': ('username', 'password1', 'password2')}),
        ('추가 정보', {'fields': ('phone')})
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Shelter)
admin.site.register(ShelterInformation)
admin.site.register(Message)