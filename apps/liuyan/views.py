from django.shortcuts import render

# Create your views here.


def getstart(request):

    return render(request=request, template_name='start.html')