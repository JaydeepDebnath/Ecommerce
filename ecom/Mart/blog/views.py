from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request , 'blog/index.html')

def compellingTopic(request):
    return HttpResponse("Check your compelling topic ")

def searchUrl(request):
    return HttpResponse("Search youtr friendly Url")

def author(request):
    return HttpResponse("About our Author")

def tableContent(request):
    return render(request, 'blog/table.html')

def introduction(request):
    return HttpResponse("Our page Introduction ")

def conclusion(request):
    return HttpResponse("Page Conclusion")