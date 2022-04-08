from django.http.response import HttpResponseRedirect
from django.shortcuts import render
import markdown
from . import util
from django.urls import reverse


def index(request):
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
    

