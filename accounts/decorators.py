from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def maker_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/list'):  
 
    actual_decorator = user_passes_test(
        lambda u: u.is_maker,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def checker_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/list'):

    actual_decorator = user_passes_test(
        lambda u: u.is_checker,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator