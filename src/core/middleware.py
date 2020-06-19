from django.conf import settings
from django.utils.translation import activate
import re


def ForceInRussianMiddleware(get_response):
    """
    Force lanuage in admin
    """
    def middleware(request):
        if re.match(".*admin/", request.path):
            activate("ru")
        return get_response(request)
    return middleware
