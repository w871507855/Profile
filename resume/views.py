from django.views import generic

from .models import Profile


class ShowResume(generic.DetailView):
    template_name = 'resume/profile.html'
    context_object_name = 'profile'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ShowResume, self).get_context_data(**kwargs)

        # get single profile via URLconf kwargs.
        obj = Profile.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))
        context['Qualifications'] = obj.qualifications_set.all()
        context['Achievements'] = obj.achievements_set.all().order_by('-to_date')
        context['Education'] = obj.education_set.all().order_by('-to_date')
        return context


# A view just for print.
class ResumePrint(ShowResume):
    template_name = 'resume/print.html'

