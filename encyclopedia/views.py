from django import forms
from django.shortcuts import redirect, render
import markdown
from . import util
from django.urls import reverse
from .forms import EditForm
from random import randrange

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
    
    return redirect(reverse("notfound"))


def editPage(request, title):
    if request.method=="POST":
        form = EditForm(request.POST)
        
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title,content)
            return redirect(reverse("title", args={title}))
    
    content = util.get_entry(title)
    form = EditForm()
    form.fields['title'].widget=forms.HiddenInput()
    form.fields['content'].initial=content
    form.fields['title'].initial=title
    return render(request, "encyclopedia/editpage.html",{
        "title": title,
        "form": form,
    })


def createPage(request):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is None:
                util.save_entry(title, content)
                return redirect(reverse("title", args={title}))
            
            return render(request, "encyclopedia/createpage.html", {
                "h1": "Create New Page",
                "form": form,
                "error": "This Title Alredy Exists!!"
            })
            
    return render(request,"encyclopedia/createpage.html", {
        "h1": "Create New Page",
        "form": EditForm(),
    })


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


def randomPage(request):
    list = util.list_entries()
    i = randrange(0, len(list))
    title = list[i]
    print(i,title)
    return redirect(reverse("title", args={title}))


def notfound(request):
    return render(request, "encyclopedia/notfound.html")
    