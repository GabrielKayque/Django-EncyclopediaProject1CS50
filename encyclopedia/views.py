from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
import markdown
from . import util
from django.urls import reverse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

    
def title(request, title=None, clear=None):
    print(clear)
    if util.get_entry(title) != None:
        content = markdown.markdown(util.get_entry(title))
        return render(request, "encyclopedia/title.html", {
            "title" : title, "content": content 
        })
    else:
        return HttpResponseRedirect(reverse("notfound"))


def notfound(request):
    return render(request, "encyclopedia/notfound.html")


def search(request):
    query = request.GET.get("q")
    if util.get_entry(query) is not None:
        return redirect(reverse("title", args={query}))
    
    entries = util.list_entries()
    matchs = []
    for entry in entries:
        if query.upper() in entry.upper() or entry.upper() in query.upper():
            matchs.append(entry)
    if matchs:
        return render(request, "encyclopedia/search.html", {
            "entries": matchs, "query": query
        })
        
    return redirect(reverse("notfound"))    
    

    
        

    
        
        
        
        
        
    

