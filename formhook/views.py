from django.views.generic.edit import FormView


from .forms import PersonalInfo


class Introduction(FormView):
    template_name = 'formhook/Introduction.html'
    form_class = PersonalInfo





