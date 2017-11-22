from django.contrib import admin
from .models import PersonalInformation, Education, WorkExperience, WorkExperiencePortfolio, Language


# -----------------------------------------------------------------------------
# PERSONAL INFORMATION
# -----------------------------------------------------------------------------
@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'phone_number', 'email']


# -----------------------------------------------------------------------------
# CURRICULUM
# -----------------------------------------------------------------------------
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'from_date', 'to_date']


class WorkExperiencePortfolioChild(admin.TabularInline):
    model = WorkExperiencePortfolio
    extra = 0


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'from_date', 'to_date']
    inlines = [WorkExperiencePortfolioChild]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language', 'mother_tongue', 'understanding_listening', 'understanding_reading',
                    'speaking_interaction', 'speaking_production', 'writing']
    list_filter = ['mother_tongue']
    search_fields = ['language']
