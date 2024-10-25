from cars.models import Car 
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# usando CBV(buscando todos os carros e filtrando tb)
class CarsListView(ListView):
    model = Car
    template_name = 'car/request.html'
    context_object_name = 'cars'

    # filtrando o carro
    def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset

# Usando CreateView, igual NewCarView porem mais enxuto
@method_decorator(login_required, name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car/new_car.html'
    success_url = reverse_lazy('cars_request')


# Usando DetailView
class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car_detail.html'


# usando UpdateView
@method_decorator(login_required, name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car/car_update.html'
    # success_url = reverse_lazy('cars_request')

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

# usando DeleteView
@method_decorator(login_required, name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/car_delete.html'
    success_url = reverse_lazy('cars_request')
