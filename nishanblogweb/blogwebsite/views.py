from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article
from .models import RegistrationForm

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("Invalid Details")
    else:
        form = RegistrationForm
    return render(request, 'register.html', {'form': form})
        
            
    