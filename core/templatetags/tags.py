from django import template
from datetime import datetime

from core.models import Tag

register = template.Library()


@register.inclusion_tag("tags_dropdown.html")
def tags_dropdown():
    """
    Возвращает dropdown со ссылками на поиск по тегу
    """
    tags = Tag.objects.all()
    return {"tags": tags}
