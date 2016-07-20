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


from django.template import loader, RequestContext
from django.http import HttpResponse


def custom_proc(request):
    # "A context processor that provides 'app', 'user' and 'ip_address'."
    return {'app': 'My app',
            'user': request.user,
            'ip_address': request.META['REMOTE_ADDR'],
            # 'sql_queries':  request.debug,
            'request': request,
            'testp': 'AAA\nBBB\nCCC'
            }


def test(request):
    t = loader.get_template('formhook/test.html')
    c = RequestContext(request, {'message': 'I am view 1.'}, processors=[custom_proc])
    return HttpResponse(t.render(c))


