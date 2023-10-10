from django.http import HttpResponse
from functools import wraps
import logging


def log_request(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Log the incoming request
        logging.info(f"Request: {request.method} {request.path}")
        return view_func(request, *args, **kwargs)
    return wrapper


'''Apply the decorator to a view as below example:'''


@log_request
def my_view(request):
    # Your view logic
    return HttpResponse("Hello, World!")
