from django.db import models


class PersonalInfor(models.Model):
    name = models.CharField(max_length=50, verbose_name='You name')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of birth')
    email = models.EmailField(verbose_name='Email', unique=True)
    introduction = models.TextField(verbose_name='Introduction of yourself', blank=True)

    def __str__(self):
        return self.name







