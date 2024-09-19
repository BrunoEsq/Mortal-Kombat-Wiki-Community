from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Player, Coach

class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'user_type')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

class JugadorAdmin(admin.ModelAdmin):
    model = Player
    list_display = ('user',)
    search_fields = ('user__username',)

class EntrenadorAdmin(admin.ModelAdmin):
    model = Coach
    list_display = ('user',)
    search_fields = ('user__username',)

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Player, JugadorAdmin)
admin.site.register(Coach, EntrenadorAdmin)
