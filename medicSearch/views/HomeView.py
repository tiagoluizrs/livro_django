from django.shortcuts import render

def home_view(request):
    return render(request, template_name='home/home.html', status=200)