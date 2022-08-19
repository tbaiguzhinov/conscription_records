from django.contrib import admin

from regs.models import Member, Personnel

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    ordering = ['employee']

class MemberInline(admin.TabularInline):
    model = Member
    extra = 0

@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    ordering  = ['last_name']
    inlines = [
        MemberInline,
    ]
