from django.contrib import admin

from .models import Profile, Qualifications, Achievements, Education


class QualificationsInline(admin.StackedInline):
    model = Qualifications


class AchievementsInline(admin.StackedInline):
    model = Achievements
    extra = 4


class EducationInline(admin.StackedInline):
    model = Education
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Profile', {'fields': ['name', 'phone', 'email']}),

    ]
    inlines = [Qualifications, Achievements, Education]


admin.site.register(Profile)
admin.site.register(Qualifications)
admin.site.register(Achievements)
admin.site.register(Education)
