from django.shortcuts import render
from .models import Pizza

# Create your views here.
from .models import Topic
def index(request):
    return render(request, 'pizzeria_logs/index.xhtml')

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria_logs/pizzas.xhtml', context)