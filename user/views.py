
from django.views.generic import ListView, DetailView

from .models import User

# Create your views here.


class UserListView(ListView):
    model = User
    template_name = 'home.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'detail.html'
