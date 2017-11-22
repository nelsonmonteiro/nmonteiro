from rest_framework import serializers
from .models import PersonalInformation, Education, WorkExperience, WorkExperiencePortfolio, Language


# -----------------------------------------------------------------------------
# PERSONAL INFORMATION
# -----------------------------------------------------------------------------
class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = ['id', 'name', 'date_of_birth', 'age', 'role', 'short_description', 'about', 'address', 'phone_number',
                  'email', 'website', 'facebook', 'twitter', 'linkedin', 'github', 'skype', 'hobbies', 'other_skills']


# -----------------------------------------------------------------------------
# CURRICULUM
# -----------------------------------------------------------------------------
class CurriculumDateBaseSerializer(serializers.ModelSerializer):
    from_date = serializers.CharField(source='get_from_date_display')
    to_date = serializers.CharField(source='get_to_date_display')

    class Meta:
        fields = ['id', 'from_date', 'to_date', 'title', 'organization']


class EducationSerializer(CurriculumDateBaseSerializer):
    class Meta(CurriculumDateBaseSerializer.Meta):
        model = Education


class WorkExperiencePortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperiencePortfolio
        fields = ['id', 'organization', 'project', 'description',
                  'image', 'key_technologies', 'main_activities']


class WorkExperienceSerializer(CurriculumDateBaseSerializer):
    portfolio = WorkExperiencePortfolioSerializer(many=True)

    class Meta:
        model = WorkExperience
        fields = CurriculumDateBaseSerializer.Meta.fields + ['description']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language', 'mother_tongue', 'understanding_listening', 'understanding_reading',
                  'speaking_interaction', 'speaking_production', 'writing']
