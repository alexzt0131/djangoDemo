from django.shortcuts import render

# Create your views here.


def getstart(request):

    print(request.POST)

    return render(request=request, template_name='start.html')