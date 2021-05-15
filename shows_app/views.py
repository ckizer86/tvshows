from django.shortcuts import render, redirect
from .models import *
from time import gmtime, localtime, strftime

# Create your views here.

def index(request):
    return redirect('/shows')

def shows(request):

    context = {
        "all_movies": Movie.objects.all(),
        "all_networks": Network.objects.all(),
        
    }
    
    return render(request, "shows.html", context)

def new(request):
    
    context = {
        "all_networks": Network.objects.all(),
    }
    return render(request, "new.html", context)

def create(request):
    network_id = request.POST["network"]
    network = Network.objects.get(id=network_id)
    title = request.POST["title"]
    release_date = request.POST["release_date"]
    description = request.POST["description"]
    this_movie = Movie.objects.create(network=network, title=title, desc=description, release_date=release_date)

    return redirect(f'/shows/{this_movie.id}')

def view_show(request,id):
    this_show = Movie.objects.get(id=id)

    context={
        "this_show": this_show,
        "exnetworks": Network.objects.exclude(network=id),
    }
    return render(request, "view_show.html", context)

def edit(request,id):
    this_show = Movie.objects.get(id=id)
    month = '{:02d}'.format(this_show.release_date.month)
    day = '{:02d}'.format(this_show.release_date.day)

    context={
        "this_show": this_show,
        "exnetworks": Network.objects.exclude(network=id),
        "month": month,
        "day": day,
    }

    return render(request, "edit_show.html", context)

def update(request,id):
    this_movie = Movie.objects.get(id=id)
    networkid = request.POST['network']
    network = Network.objects.get(id=networkid)
    title = request.POST['title']
    description = request.POST['description']
    release_date = request.POST['release_date']

    this_movie.network = network
    this_movie.title = title
    this_movie.desc = description
    this_movie.release_date = release_date
    this_movie.save()

    return redirect(f'/shows/{id}')

def destroy(request,id):
    this_movie = Movie.objects.get(id=id)
    this_movie.delete()
    return redirect('/shows')

def add_network(request):
    netname = request.POST["add_network"]
    Network.objects.create(name=netname)
    
    return redirect("/shows/new")