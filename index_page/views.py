from django.shortcuts import render


def index(request):
    return render(request, 'index_page/home_page.html')
