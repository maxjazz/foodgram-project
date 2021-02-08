from django.core.exceptions import ValidationError
from .models import Recipe

def not_zero(value):
    if value == 0:
        raise ValidationError(
            _('%(value)s can not be zero'),
            params={'value': value},
        )


def get_counter(user):
    return Recipe.objects.filter(
        shopping_list__user=user).count


def get_url(current_tag, available_tags):
    answer = []
    for tag in available_tags:
        answer.append(tag)
    if current_tag in answer:
        answer.remove(current_tag)
    else:
        answer.append(current_tag)
    return "&tag=".join(answer)
