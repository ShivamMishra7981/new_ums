from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Manager,Executive

#exclusively defining to add in one user form for admin
class ManagerInline(admin.StackedInline):
    model = Manager
    can_delete = False
    verbose_name_plural = 'Manager'

class ExecutiveInline(admin.StackedInline):
    model = Executive
    can_delete = False
    verbose_name_plural = 'Executive'


#admin functionality to include manager and executive 
class UserAdmin(BaseUserAdmin):
    inlines = (ManagerInline, ExecutiveInline)
    list_display = ('username', 'email', 'is_manager', 'is_executive')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_manager', 'is_executive','groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, UserAdmin) 
admin.site.register(Manager)
admin.site.register(Executive)