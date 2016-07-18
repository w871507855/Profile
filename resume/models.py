# import from python standard module
import datetime

# import from app
from django.db import models
from django.utils import timezone


# Basic information
class Profile(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=254, blank=False)

    def __str__(self):
        return self.name


# Define a common ABSTRACT model for Achievements & Education.
class CommonInfo(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    organisation = models.CharField(max_length=150)
    from_date = models.DateField(verbose_name="Since")
    to_date = models.DateField(verbose_name="To")
    detail = models.TextField(verbose_name="Detail Description")

    def __str__(self):
        return self.organisation

    def is_date_validate(self):
        # now = datetime.datetime.now()
        # TypeError: can't compare offset-naive and offset-aware datetimes.
        now = timezone.now()
        return now > self.to_date > self.from_date

    class Meta:
        abstract = True
        ordering = ['to_date']


class Qualifications(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    detail_item = models.TextField()


class Achievements(CommonInfo):
    pass


class Education(CommonInfo):
    pass


