from django.contrib import admin
from .models import Experience, Education, Award

# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Experience, ExperienceAdmin)

class EducationAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Education, EducationAdmin)

class AwardAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Award, AwardAdmin)