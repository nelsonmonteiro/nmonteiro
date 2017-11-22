from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView, Response
from rest_framework import status
from .serializers import PersonalInformationSerializer, WorkExperienceSerializer, LanguageSerializer, \
    EducationSerializer
from .models import PersonalInformation, WorkExperience, Education, Language


# -----------------------------------------------------------------------------
# PERSONAL INFORMATION
# -----------------------------------------------------------------------------
class PersonalInformationDetail(RetrieveAPIView):
    serializer_class = PersonalInformationSerializer

    def get_object(self):
        return PersonalInformation.objects.latest()


# -----------------------------------------------------------------------------
# CURRICULUM
# -----------------------------------------------------------------------------
class CurriculumDetail(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        personal_information = PersonalInformation.objects.latest()
        work_experience = WorkExperience.objects.prefetch_related('portfolio')
        education = Education.objects.all()
        languages = Language.objects.all()

        return Response({
            'personal_information': PersonalInformationSerializer(personal_information).data,
            'education': EducationSerializer(education, many=True).data,
            'work_experience': WorkExperienceSerializer(work_experience, many=True).data,
            'languages': LanguageSerializer(languages, many=True).data,
        })