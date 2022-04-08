from django.http.response import HttpResponseRedirect
from django.shortcuts import render
import markdown
from . import util
from django.urls import reverse


def index(request):
    print(util.list_entries())
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

    
    
def title(request, title=None):
    if util.get_entry(title) != None:
        content = markdown.markdown(util.get_entry(title))
        return render(request, "encyclopedia/title.html", {
            "title" : title, "content": content 
        })
    return HttpResponseRedirect(reverse("notfound"))


def notfound(request):
    return render(request, "encyclopedia/notfound.html")


def search(request):
    query = request.GET.get("q")
    if util.get_entry(query) != None:
        content = markdown.markdown(util.get_entry(query))
        return render(request, "encyclopedia/title.html", {
            "title" : query.capitalize, "content": content 
        })
        
    entries = util.list_entries()
    matchs = []    
    for entry in entries:
        if query.upper() in entry.upper():
            matchs.append(entry)
            print(f"entrada {entry}, lista atual: {matchs}")
    if matchs != []:
        return render(request, "encyclopedia/search.html", {
        "entries": matchs, "query": query
    })
    
    return HttpResponseRedirect(reverse("notfound"))      
    
        
        
        
        
        
    

