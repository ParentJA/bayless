from django.http import HttpResponseBadRequest

import json


def get_request_data(request, *parameters):
    data = request.GET

    if request.method == 'POST':
        data = request.POST

    if not data:
        try:
            data = json.loads(request.body)
        except ValueError:
            return HttpResponseBadRequest('The request must contain data.')

    if not data or not all([param in data for param in parameters]):
        return HttpResponseBadRequest('The following keys must be specified in the request: a, b.')

    return data