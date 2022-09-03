import json

from django.http import HttpResponse

response = {
    200: 'Success',
    400: 'Invalid Argument',
    500: 'Mapping Key Error'
}


def CustomResponse(code, message, data):
    responseData = {
               "code": code,
               "message": message,
               "data": data,
           }
    return HttpResponse(json.dumps(responseData), content_type = "application/json")


def DefaultResponse(code, data):
    responseData = {
               "code": code,
               "message": response[code],
               "data": data,
           }
    return HttpResponse(json.dumps(responseData), content_type = "application/json")