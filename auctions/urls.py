from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing", views.create_listing, name="create_listing"),
    path("<int:user_id>/add", views.add_listing, name="add_listing"),
    path("<int:listing_id>", views.view_listing, name="view_listing"),
    path("<int:listing_id>/bid", views.bid, name="bid"),
    path("<int:listing_id>/closeAuction", views.close_auction, name="close_auction")
]
