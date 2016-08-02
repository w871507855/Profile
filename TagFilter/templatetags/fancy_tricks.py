from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


register = template.Library()


def addp(value):
    '''
    addp is a filter that converts a string to another format string containing html <p> tags.
    :param value: string containing '\n'
    :return: String containing <p></p> html tags.
    '''
    # Just in case there is html tags in value
    value = conditional_escape(value)

    # Split any text by '\n',
    # Such as, 'aaaa\nbbb\nccc' convert to ['aaaa', 'bbb', 'ccc']
    list_str = value.split('\n')

    # Now, the list_str will looks like this: ['<p>aaaa</p>', '<p>bbb</p>', '<p>ccc</p>']
    list_str = ['<p>' + x + '</p>' for x in list_str]
    # Finally, return all we want: '<p>aaaa</p><p>bbb</p><p>ccc</p>'
    return mark_safe(''.join(list_str))

register.filter('addp', addp)

'''
@template.Library.simple_tag
def query_list_all(obj, form='p', max_entry=5)


    :param obj: to be a query object;
    :param form: 'p'--> <p> | 'li'--> <li> | 'dt'--> <dt>;
    :param max_entry: obj.objects.all[:max_entry], the maximum entry allowed;
    :return: If obj.objects.all() == [aaa, bbb, ccc], then:
    if form='p', <p>aaa</p><p>bbb</p><p>ccc</p>
    if form='li', <li>aaa</li><li>bbb</li><p>ccc</li>
    if form='dt', <dt>aaa</dt><dt>bbb</dt><p>ccc</dt>

    try:
        entry_list = obj.objects.all()[:max_entry]

    except:
        return ''

register.tag('query_list_all', query_list_all)
'''