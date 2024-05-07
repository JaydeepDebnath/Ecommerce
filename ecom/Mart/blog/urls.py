from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name = "BlogHome"),
    path('compellingTopic',views.compellingTopic,name ="compellingTopic"),
    path('searchUrl',views.searchUrl,name = "searchUrl"),
    path('author',views.author,name = "author"),
    path('tableContent',views.tableContent,name = "tableContent"),
    path('introduction',views.introduction,name = "introduction"),
    path('conclusion',views.conclusion,name = "conclusioon"),

]