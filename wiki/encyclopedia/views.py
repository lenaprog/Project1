from email import message
from django.shortcuts import render, redirect
import markdown2 
from django import forms
from django.http import HttpResponse


from . import util


"""class Search(forms.Form):
    item = forms.CharField(label="Search request", widget=forms.TextInput(attrs={'class' : 'myfieldclass', 'placeholder': 'Search'})) 
"""
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries" : util.list_entries(),
        
    })
def search(request):
    term = request.GET.get("q")
    entries = util.search_entry(term)
    if term:
        return redirect("page", term)
    else:
        return render(request, "encyclopedia/search.html", {
        "entries" : entries,
        })

def new_entry(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if util.get_entry(title):
            return HttpResponse ("Entry already exists")
        else:
            util.save_entry(title, content)
            return redirect ("encyclopedia/page.html", title)
    return render(request, "encyclopedia/newentry.html")


def page(request, title):
    entry = util.get_entry(title)
    if (entry is not None):
        entry = markdown2.markdown(entry)

        context = {
            "entry": entry,
            "title": title,
        }
        return render(request, "encyclopedia/page.html", context)


        
        
        
        
        
       

        
