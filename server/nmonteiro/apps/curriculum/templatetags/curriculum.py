from django import template
from ..models import PersonalInformation, WorkExperience, Education, Language

register = template.Library()


@register.assignment_tag
def get_curriculum():
    return {
        'personal_information': PersonalInformation.objects.latest(),
        'work_experience': WorkExperience.objects.prefetch_related('portfolio'),
        'education': Education.objects.all(),
        'languages': Language.objects.all(),
    }

