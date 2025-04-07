from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Crud

class CrudListView(ListView):
    model = Crud
    template_name = 'blog/crud_list.html'  
    context_object_name = 'articles'


class CrudCreateView(CreateView):
    model = Crud
    fields = '__all__'
    template_name = 'blog/crud_form.html'
    success_url = reverse_lazy('crud_list')


class CrudUpdateView(UpdateView):
    model = Crud
    fields = '__all__'
    template_name = 'blog/crud_form.html'
    success_url = reverse_lazy('crud_list')
    
    def form_valid(self, form):  
        
        return super().form_valid(form)  

class CrudDeleteView(DeleteView):
    model = Crud
    template_name = 'blog/crud_confirm_delete.html'
    success_url = reverse_lazy('crud_list')