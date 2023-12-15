# from django.shortcuts import render

# # Create your views here.
# from django.views.generic.list import ListView
# from cardquest.models import PokemonCard, Trainer
# class HomePageView(ListView):
#     model = PokemonCard
#     context_object_name = 'home'
#     template_name = "home.html"


# class TrainerList(ListView):
#     model = Trainer
#     context_object_name = 'trainer'
#     template_name = "trainer.html"
#     paginate_by = 15

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
#        # c ontext = super(HomePageView, self).get_context_data(**kwargs)
#         # return context
from django.shortcuts import render

from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer,Collection
# from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from cardquest.models import PokemonCard, Trainer
from cardquest.forms import TrainerForm,CollectionForm,PokemonCardForm
from django.urls import reverse_lazy
import json
class PokemonCardListView(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemon-card.html"
    json_file_path = 'C:/Users/admin/cardquest/appdev01/projectsite/cardquest/data/pokemon_data.json'
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context
    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('pokemons', [])


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context    

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = "collection.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  
      
# class PokemonCard(ListView):
#     model = PokemonCard
#     context_object_name = 'pokemoncard'
#     template_name = "pokemon-card.html"
#     paginate_by = 5

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
    
class TrainerCreateView(CreateView):
  model = Trainer
  form_class = TrainerForm
  template_name = 'trainer_add.html'
  success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_add.html'
    success_url = reverse_lazy('collection-list')

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_edit.html'
    success_url = reverse_lazy('collection-list')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection_del.html'
    success_url = reverse_lazy('collection-list')

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection_list'
    template_name = 'collection.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon-card_add.html'
    success_url = reverse_lazy('pokemoncard-list')

class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon-card_edit.html'
    success_url = reverse_lazy('pokemoncard-list')

class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'pokemon-card_del.html'
    success_url = reverse_lazy('pokemoncard-list')
   