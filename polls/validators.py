from django.core.exceptions import ValidationError
from datetime import datetime

def validate_school_email(value):
    if not '.edu' in value:
        raise ValidationError('A valid school email must be entered in')
    else:
        return value


def validate_year_birtday(value):
    if datetime.now().date() < value :
        raise ValidationError('A valid year of birtday must be entered in')
    else :
        return value
