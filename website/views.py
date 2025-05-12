from django.shortcuts import render
from .models import MyApp
# Create your views here.
def index(request):
    apps = MyApp.objects.all()
    return render(request, 'website/index.html', {'apps': apps})