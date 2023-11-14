import settings
import re


def check_date(value):
    return (re.search(settings.DATE_TEMP1, value)
            or re.search(settings.DATE_TEMP2, value))


def check_phone(value):
    return bool(re.search(settings.PHONE_TEMP, value))


def check_email(value):
    return bool(re.search(settings.EMAIL_TEMP, value))


def check_text(value):
    return bool(value)


def check_type(value):
    value = value.strip()
    if check_date(value):
        return 'date'
    elif check_phone(value):
        return 'phone'
    elif check_email(value):
        return 'email'
    elif check_text(value):
        return 'text'
