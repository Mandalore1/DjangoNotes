from django import template

register = template.Library()


@register.simple_tag
def add_query_params(request, key, value):
    """
    Возвращает строку запроса, добавив новый или изменив старый параметр запроса
    """
    qd = request.GET.copy()
    qd[key] = value
    return qd.urlencode()
