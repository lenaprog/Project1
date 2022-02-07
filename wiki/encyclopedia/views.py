from email import message
from django.shortcuts import render, redirect
import markdown2 
from django import forms


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
    
    return render(request, "encyclopedia/search.html", { 
    "entries": entries
    } )



def page(request, title):
    entry = util.get_entry(title)
    if (entry is not None):
        entry = markdown2.markdown(entry)

        context = {
            "entry": entry,
            "title": title,
        }
        return render(request, "encyclopedia/page.html", context)


        
        
        
        
        
       

        
