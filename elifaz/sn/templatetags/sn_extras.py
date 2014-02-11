from django import template

register = template.Library()

@register.filter
def pippo(value):
    """Removes all values of arg from the given string"""
    return value.replace('BPM', '<abbr title="Banca Popolare di Milano">BPM</abbr>').replace('Rino Snaidero Scientific Foundation', '<a href="http://www.snaiderofoundation.org/">Rino Snaidero Scientific Foundation</a>')
