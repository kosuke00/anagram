from django.shortcuts import render
from collections import Counter
from .anagrams import *
from django.urls import reverse
# Create your views here.
def homepage(request):
    return render(request,"home.html")

def anagram(request):
    input_name = request.POST["user_name"]
    """help user built anagram phrase from thier name"""
    name = "".join(input_name.lower().split())
    name = name.replace("-","")
    limit = len(name)
    phrase = request.POST["chosen_word"]
    temp_phrase = phrase.replace(" ","")
    selected_word = request.POST["ana_word"]
    choice, name = process_choice(name,selected_word)
    phrase += choice + " "
    ana = find_anagrams(name)
    txt = f"current anagram phrase :"


    return render(request,"anagram_words.html",{"name":name, "ana":ana, "txt":txt, "choice":phrase})
    
