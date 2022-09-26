from django.views.generic import ListView, DetailView
from .models import Cheese

# Create your views here.
# Simple view that lists all the cheeses in a single page.
# The Cheese model is imported using a relative import becuase we are importing from within the same app.
class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese