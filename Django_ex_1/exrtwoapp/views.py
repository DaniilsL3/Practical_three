from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_MVT_view(request):
    context = {}
    return render(request, "index.html", context)
