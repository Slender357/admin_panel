from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ("name",)

    # Поиск по полям
    search_fields = ("name", "id")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ("full_name",)

    # Поиск по полям
    search_fields = ("full_name", "id")


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork
    autocomplete_fields = ("genre",)


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork
    autocomplete_fields = ("person",)


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (
        GenreFilmworkInline,
        PersonFilmworkInline,
    )
    # Отображение полей в списке
    list_display = ("title", "type", "creation_date", "rating", "get_genres")

    # Фильтрация в списке
    list_filter = ("type",)

    # Поиск по полям
    search_fields = ("title", "description", "id")
    list_prefetch_related = ("genres",)

    def get_queryset(self, request):
        queryset = (
            super().get_queryset(request).prefetch_related(*self.list_prefetch_related)
        )
        return queryset

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = _("genres_film")
