from django.urls import path
from .views import homepage,anagram,process_choice
urlpatterns=[
path("",homepage, name="home"),
path("anagram",anagram, name="anagram_words"),
path("process_choice",process_choice,name="choice")
]
