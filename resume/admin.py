from django.contrib import admin

from .models import Profile, Qualifications, Achievements, Education


class QualificationsInline(admin.StackedInline):
    model = Qualifications
    extra = 1


class AchievementsInline(admin.StackedInline):
    model = Achievements
    extra = 2


class EducationInline(admin.StackedInline):
    model = Education
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    fields = ['name', 'phone', 'email']
    list_display = ('name', 'phone', 'email', 'show_url')
    # view_on_site = False
    inlines = [QualificationsInline, AchievementsInline, EducationInline]


admin.site.register(Profile, ProfileAdmin)