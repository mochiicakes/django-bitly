from django.urls import path
from . views import index
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('<str:link_slug>/', views.root_link, name="root-link"),
    path('link/create', views.add_link, name="create-link"),
]
