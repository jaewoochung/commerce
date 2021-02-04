from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .models import Listing


# item_id = 0 # id to pass when creating a listing

def index(request):
    all_listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": all_listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    return render(request, "auctions/create_listing.html")

def add_listing(request, user_id):
    if request.method == "POST":
        all_listings = Listing.objects.all()
        item_id = len(all_listings)
        title = request.POST["title"]
        description = request.POST["description"]
        bid = request.POST["bid"]
        image = request.POST["image"]
        num_bids = request.POST["num_bids"]
        # user = User.objects.get(pk=user_id)
        listing = Listing(item_id, title, description, bid, image, num_bids, user_id)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
        # return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

def view_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    listingUser = User.objects.get(pk=listing.user_id)
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "listingUser": listingUser
        # "user": listing.user
    })

def bid(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(id=listing_id)
        bid_track = listing.num_bids
        bid_track += 1
        new_bid = request.POST["bid"]
        listing.bid = new_bid
        listing.num_bids = bid_track

        bidder = request.POST["bidder"]
        listing.bidder = bidder
        listing.save()
        return render(request, "auctions/bid.html", {
            "listing": listing
        })

def close_auction(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(id=listing_id)
        listing.delete()
        return render(request, "auctions/closeAuction.html")
