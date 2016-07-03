from django.http import HttpResponse
from django.template import loader


def helloPage(request):
    template = loader.get_template('home/homepage.html')
    context = {
        'greeting': 'Hi, everyone'
    }
    return HttpResponse(template.render(context, request))