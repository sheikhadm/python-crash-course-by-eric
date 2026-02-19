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

def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeria_logs/toppings.xhtml', context)