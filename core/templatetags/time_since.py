from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def time_since_24h(created_time):
    """
    Возвращает время, прошедшее с заданного момента до текущего, если оно не превышает 24 часов,
    иначе возвращает заданный момент
    """
    time_passed = datetime.now(tz=created_time.tzinfo) - created_time
    if time_passed.days > 0:
        return created_time.strftime("%d.%m.%Y в %H:%M")

    seconds = time_passed.seconds
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    result = ""
    if hours > 0:
        result += f"{hours} ч. "
    if minutes > 0:
        result += f"{minutes} мин. "

    result += f"{seconds} с. назад"
    return result
