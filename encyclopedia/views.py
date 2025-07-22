from django.shortcuts import render
import markdown 
from random import choice as random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
# search result with short searching
def search(request):
    if request.method == "POST":
        query = request.POST["q"]
        entry_content = md_to_html(query)
        if entry_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": query,
                "content": entry_content
            })
        else:
            entries = util.list_entries()
            matching_entries = (entry for entry in entries if query.lower() in entry.lower())
            return render(request , "encyclopedia/index.html", {
                "search" : "With your Search ",
                "entries": matching_entries
            })
# converter md to html
def md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content is None:
        return None
    else:
        return markdowner.convert(content)
# content of the saved entries
def entry(request , title):
    entry_content = md_to_html(title)
    if entry_content == None:
        return render(request , "encyclopedia/error.html")
    else:
        return render (request , "encyclopedia/entry.html",{
            "title" : title,
            "content" : entry_content 
        })

# new Page
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    elif request.method == "POST":
        title = request.POST["title"]   
        content = request.POST["content"]
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html")
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": md_to_html(title)
            })

# Rendom Page 
def rendom(request):
    entries = random(util.list_entries())
    entry_content = md_to_html(entries)
    return render (request , "encyclopedia/entry.html",{
            "title" : entries,
            "content" : entry_content 
        })

    
# Edit Page
def edit_page(request, title):
    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": md_to_html(title)
        })
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            "title": title,
            "content": content
        })



