from django import template
from django.utils.safestring import SafeString

register = template.Library()

WIDTH = 600
MAIN_COLOR = 'rgb(255, 171, 64)'


@register.simple_tag
def style(name, extra=None):
    if name == 'base':
        style = "font-size: 14px; font-family: Roboto, 'Helvetica Neue', " \
                "Helvetica, Arial, sans-serif; color: #333333; line-height: 1.5; font-weight: 400;"

    elif name == 'section':
        style = 'max-width: %s; margin: 0 auto; padding: 60px 0;' % WIDTH

    elif name == 'action-section':
        style = 'max-width: %s; margin: 0 auto; padding: 20px 0;' % WIDTH

    elif name == 'footer-section':
        style = 'max-width: %s; margin: 0 auto; padding: 30px 0;' % WIDTH

    elif name == 'button':
        style = 'background: %s; border-radius: 2px; color: #ffffff; font-size: 15px; text-transform: uppercase; ' \
                'line-height: 50px; letter-spacing: 0.5px; padding: 0 30px; vertical-align: middle;' \
                'display: inline-block; text-decoration: none;' % MAIN_COLOR

    elif name == 'a':
        style = 'color: inherit; text-decoration: none;'

    elif name == 'h2':
        style = 'margin: 0 0 60px; font-weight: 100; font-size: 33px;'

    elif name == 'h4':
        style = 'margin: 30px 0 5px; font-weight: 600; font-size: 1.1em;'

    elif name == 'h5':
        style = 'margin: 14px 0; font-weight: bold; font-size: inherit;'

    elif name == 'date':
        style = 'margin-bottom: 14px; font-weight: bold; font-style: italic; color: %s;' % MAIN_COLOR

    elif name == 'experience':
        style = 'margin-bottom: 50px; padding-bottom: 50px; border-bottom: 1px solid #eee;'

    elif name == 'project':
        style = 'margin-bottom: 40px;'

    elif name == 'education':
        style = 'margin-bottom: 30px;'

    else:
        style = ''

    return SafeString('style="%s %s"' % (style, extra or ''))


