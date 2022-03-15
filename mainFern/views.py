from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Barnsley(request):
    
    return render(request,'Main/Barnsley.html')
