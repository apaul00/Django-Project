from django.shortcuts import render, redirect

from .forms import PizzaForm
from .models import Pizza, Topping

# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas':pizzas} #use pizza key in html file, value in views file

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()

    context = {'pizza':pizza, 'toppings':toppings}
    
    return render(request, 'pizzas/pizza.html', context)

def new_comment(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save()


            return redirect('pizzas:pizzas')

    context = {'form': form}
    return render(request, 'pizzas/new_comment.html', context)

    