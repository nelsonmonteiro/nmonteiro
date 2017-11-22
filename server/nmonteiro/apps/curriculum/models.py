import datetime
from tinymce.models import HTMLField
from sorl.thumbnail.fields import ImageField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from apps.core.utils.models import get_namedtuple_choices, upload_to


# -----------------------------------------------------------------------------
# PERSONAL INFORMATION
# -----------------------------------------------------------------------------
@python_2_unicode_compatible
class PersonalInformation(models.Model):
    class Meta:
        get_latest_by = 'id'
        verbose_name_plural = 'Personal Information'

    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    short_description = models.CharField(max_length=250, null=True, blank=True)
    about = HTMLField(null=True, blank=True)
    footer_text = HTMLField(null=True, blank=True)
    address = HTMLField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    skype = models.CharField(max_length=30, null=True, blank=True)
    hobbies = HTMLField(null=True, blank=True)
    other_skills = HTMLField(null=True, blank=True)

    @property
    def age(self):
        if self.date_of_birth:
            today = datetime.date.today()
            birthday_didnt_passed = 1 if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day) else 0
            return today.year - self.date_of_birth.year - birthday_didnt_passed
        return None

    def __str__(self):
        return self.name


# -----------------------------------------------------------------------------
# CURRICULUM
# -----------------------------------------------------------------------------
@python_2_unicode_compatible
class CurriculumDateBase(models.Model):
    class Meta:
        abstract = True
        ordering = ['-from_date']

    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, null=True, blank=True)

    def get_from_date_display(self):
        return self.from_date.strftime('%b %Y')

    def get_to_date_display(self):
        return self.to_date.strftime('%b %Y') if self.to_date else None

    def get_date_display(self):
        from_date = self.get_from_date_display()
        to_date = self.get_to_date_display()
        if not to_date:
            return 'Since %s' % from_date
        if from_date == to_date:
            return from_date
        return 'From %s to %s' % (from_date, to_date)

    def __str__(self):
        return '%s: %s' % (self.get_date_display(), self.title)


class Education(CurriculumDateBase):
    class Meta:
        verbose_name_plural = 'Education'

    image = ImageField(null=True, blank=True, upload_to=upload_to)


class WorkExperience(CurriculumDateBase):
    class Meta:
        verbose_name_plural = 'Work Experience'

    description = HTMLField(null=True, blank=True)


@python_2_unicode_compatible
class WorkExperiencePortfolio(models.Model):
    experience = models.ForeignKey(WorkExperience, related_name='portfolio')
    organization = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    project = models.CharField(max_length=100, null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    image = ImageField(null=True, blank=True, upload_to=upload_to)
    key_technologies = HTMLField(null=True, blank=True)
    main_activities = HTMLField(null=True, blank=True)

    def __str__(self):
        return '%s: %s' % (self.organization, self.project)


@python_2_unicode_compatible
class Language(models.Model):
    class Meta:
        ordering = ['-mother_tongue', 'language']

    LEVELS = get_namedtuple_choices('CURRICULUM_LANGUAGE_LEVELS', (
        ('A1', 'A1', 'A1 - Basic user'),
        ('A2', 'A2', 'A2 - Basic user'),
        ('B1', 'B1', 'B1 - Independent user'),
        ('B2', 'B2', 'B2 - Independent user'),
        ('C1', 'C1', 'C1 - Proficient user'),
        ('C2', 'C2', 'C2 - Proficient user'),
    ))

    language = models.CharField(max_length=30)
    mother_tongue = models.BooleanField(default=False)
    understanding_listening = models.CharField(max_length=2, choices=LEVELS.get_choices())
    understanding_reading = models.CharField(max_length=2, choices=LEVELS.get_choices())
    speaking_interaction = models.CharField(max_length=2, choices=LEVELS.get_choices())
    speaking_production = models.CharField(max_length=2, choices=LEVELS.get_choices())
    writing = models.CharField(max_length=2, choices=LEVELS.get_choices())

    def __str__(self):
        return self.language

