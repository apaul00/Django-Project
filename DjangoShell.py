import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza
pizza = Pizza.objects.all()

for p in pizza:
    print(p.id, '  ', p)

