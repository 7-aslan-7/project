from django.shortcuts import render

# Create your views here.
def index_1 (request):
    return render(request, 'index_2.html')