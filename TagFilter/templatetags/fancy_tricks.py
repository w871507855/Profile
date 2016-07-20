from django import template
from django.utils.safestring import mark_safe


register = template.Library()


def addp(value):
    '''
    addp is a filter that converts a string to another format string containing html <p> tags.
    :param value: string containing '\n'
    :return: String containing <p></p> html tags.
    '''

    # Split any text by '\n',
    # Such as, 'aaaa\nbbb\nccc' convert to ['aaaa', 'bbb', 'ccc']
    list_str = value.split('\n')

    # Now, the list_str will looks like this: ['<p>aaaa</p>', '<p>bbb</p>', '<p>ccc</p>']
    list_str = ['<p>' + x + '</p>' for x in list_str]
    # Finally, return all we want: '<p>aaaa</p><p>bbb</p><p>ccc</p>'
    return mark_safe(''.join(list_str))

register.filter('addp', addp)
