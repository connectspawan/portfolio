from django.contrib import admin

from .models import (
    Project,
    Contact,
    Profile,
    Skill,
    Milestone
)

admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profession', 'email', 'phone')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percentage', 'order')
    list_display_links = ('id', 'name')

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'order')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'technologies', 'created_at', 'order')
    list_editable = ('order',)
    list_filter = ('created_at',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'created_at')
    readonly_fields = ('created_at',)