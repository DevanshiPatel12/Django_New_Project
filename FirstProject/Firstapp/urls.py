from django.urls import path
from . import views         # file you're using and file you're invoking should exist in the same directory

urlpatterns = [
    path('', views.index, name = "index"),       # this path takes exactly three arguments.
    # first arguments is url --> '' this represent empty string which invoke default URL
    # second argument is file invoke --> invoking index function from views.py file
    # third argument is naming convention --> optional
    # at the end ',' comma is necessary because it is a list
    path('<int:domain_id>/', views.training_domain, name = "domain"),
    path('<int:domain_id>/candidate', views.candidate, name = "candidate"),
    #'<int:domain_id>/candidate' --> this is the format you have tu type in the URL --> 23/candidate
]