from django.views.generic.edit import FormView
from django.shortcuts import render


from .forms import PersonalInfo


class Introduction(FormView):
    template_name = 'formhook/Introduction.html'
    form_class = PersonalInfo


def intro(request):
    # POST only
    if request.method == 'POST':
        form = PersonalInfo(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'formhook/succed.html', context)
        else:
            # if data is not valid, turn back to the current page
            # with the previous from values and invalid errors.
            return render(request, 'formhook/Introduction.html', {'form': form})
    else:
        form = PersonalInfo()
        return render(request, 'formhook/Introduction.html', {'form': form})



