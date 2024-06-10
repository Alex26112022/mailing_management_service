from django import template

register = template.Library()


@register.filter()
def photo_path(path):
    if path:
        return f'/media/{path}'
    return '#'
