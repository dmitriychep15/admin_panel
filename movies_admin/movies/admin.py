from django.contrib import admin

from movies.models import (Genre, Filmwork, GenreFilmwork,
                           Person, PersonFilmwork)


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'description')
    search_fields = ('name', 'description') 


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    ordering = ('full_name',)
    list_display = ('full_name',)
    search_fields = ('full_name',)


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline)

    ordering = ('-rating',)
    list_display = ('title', 'type', 'creation_date', 'rating')
    list_filter = ('type', 'creation_date')
    search_fields = ('title', 'description')
    autocomplete_fields = ('genres', 'persons')
