from django.contrib import admin

# Register your models here.
from .models import PokemonCard,Trainer,Collection
# from .models import Collection
# admin.site.register(PokemonCard)
@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity","hp","card_type","attack","description","weakness","card_number","release_date","evolution_stage","abilities")
    search_fields = ("name",) 
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "location","email")
    search_fields = ("name",)
@admin.register(Collection)
class CollectAdmin(admin.ModelAdmin):
    list_display = ("card", "trainer", "collection_date")
    search_fields = ("collection_date",)      