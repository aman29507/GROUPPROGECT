from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser, UserAdmin)

from django.contrib import admin
from .models import MembershipRequest

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Membership Info', {'fields': ('membership_type',)}),
    )
    list_display = ('username', 'email', 'membership_type', 'is_staff', 'is_active')
    list_filter = ('membership_type', 'is_staff', 'is_active')

# Admin Panel for Membership Requests
class MembershipRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'request_date')
    list_filter = ('status',)
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(status='approved')
        self.message_user(request, "Selected membership requests have been approved.")

    def reject_requests(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, "Selected membership requests have been rejected.")

    approve_requests.short_description = "Approve selected membership requests"
    reject_requests.short_description = "Reject selected membership requests"

# Register MembershipRequest Model
admin.site.register(MembershipRequest, MembershipRequestAdmin)
# Register your models here.
