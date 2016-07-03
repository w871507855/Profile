from django.http import HttpResponse
from django.template import loader


def helloPage(request):
    template = loader.get_template('home/homepage.html')
    context = {
        'greeting':
        '''
        <p>
        Hi, Everyone. I write this Django-powered site just for capability demostration,
        and if you think I'm the staff you are looking for, I hope you can give me a offer.
        <br />
        This site is not completed and I will continue to update it.
        <br />
        Thank You!
        </p>
        '''
    }
    return HttpResponse(template.render(context, request))