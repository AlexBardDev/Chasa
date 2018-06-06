from django.shortcuts import render

# Create your views here.

def home(request):
    """This view returns the home page."""

    return render(request, "web_app/home.html")

def events(request):
    """This view returns a calendar with the events of the diving club."""

    return render(request, "web_app/events.html")

def about(request):
    """This view returns the 'about us' web page."""

    return render(request, "web_app/about.html")
