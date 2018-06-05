from django.shortcuts import render

# Create your views here.

def home(request):
    """This view returns the home page."""

    return render(request, "web_app/home.html")
