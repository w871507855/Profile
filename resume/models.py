# import from python standard module
import datetime

# import from django
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.utils.html import format_html


# Basic information
class Profile(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=254, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resume:print', kwargs={'pk': self.id})

    # 'show_url' will be added in ModelAdmin.list_display,
    # it is more direct to view this page than next page's 'view on site'.
    def show_url(self):
        url = self.get_absolute_url()
        return format_html('<a href="' + url + '">View On Site</a>')


# Define a common ABSTRACT model for Achievements & Education.
class CommonInfo(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    organisation = models.CharField(max_length=150)
    from_date = models.DateField(verbose_name="Since")
    to_date = models.DateField(verbose_name="To")
    detail = models.TextField(verbose_name="Detail Description")

    def __str__(self):
        return self.organisation

    def clean(self):
        today = timezone.now().date()
        if self.to_date > today:
            raise ValidationError({'to_date': ValidationError("Date is set to future illegally.", code='invalid')})
        if self.from_date > self.to_date:
            raise ValidationError(
                {
                    'to_date': ValidationError("To should bigger than FROM literally", code='invalid'),
                    'from_date': ValidationError("To should bigger than FROM literally", code='invalid')
                                   }
            )

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


