from django.shortcuts import render



def search_try(request):
    return render(request, "polls/search.html", {})
def home_try(request):
    return render(request, "polls/home.html", {})












