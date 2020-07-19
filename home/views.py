from django.shortcuts import render

# Creating my views

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')