from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy, reverse
# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields=['name','rank','reviewer']

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields='__all__'
    success_url = reverse_lazy('snack_list')
    # success_url = reverse('snack_list')


class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list') #mandatory
