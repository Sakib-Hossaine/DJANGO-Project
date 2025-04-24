from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Teacher, Student, ExamResult

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_teacher', 'is_student', 'is_staff')
    list_filter = ('is_teacher', 'is_student', 'is_staff')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_teacher', 'is_student', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ExamResult)