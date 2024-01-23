

# Create your views here.

#CRUD - Create Retrieve Update Delete (list)

# we will use functions
from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    
    return render(request, "listings.html", context)

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }

    return render(request, "listing.html", context)

def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/")
            
            
        context ={
            "form": form
        }
        return render(request, "listing_create.html", context)  
        
        
        
   
    context = {
        "form": form 
    }
    return render(request, "listing_create.html", context)    
