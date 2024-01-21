from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, StreamingHttpResponse, FileResponse

def http_response(request):
    return HttpResponse('<h1>HttpResponse Example</h1>')

def not_found_response(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def json_response(request):
    data = {'key': 'value'}
    return JsonResponse(data)

def streaming_response(request):
    def generator():
        yield "Hello "
        yield "world!"
    return StreamingHttpResponse(generator())

def file_response(request):
    filepath = 'Django_ex_1/response_test/files/5fz0yq.jpg'
    return FileResponse(open(filepath, 'rb'))