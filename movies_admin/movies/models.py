import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class IDMixin(models.Model):
    '''
    Inherit from this class to add UUID `id` field 
    to the model.
    '''

    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


class TimeStampedMixin(models.Model):
    '''
    Inherit from this class to add 
    `created` and `modified` datetime fields to the model.
    '''

    class Meta:
        abstract = True

    created = models.DateTimeField(
        auto_now=True
    )
    modified = models.DateTimeField(
        auto_now_add=True
    )


class FilmType(models.TextChoices):
    '''
    Possible values for `Filmwork's type` field.
    '''

    MOVIE = 'MOVIE', _('Movie')
    TV_SHOW = 'TV_SHOW', _('TV Show')


class Genre(IDMixin, TimeStampedMixin):
    '''
    Table, that stores film genres.
    '''

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    name = models.CharField(
        _('Genre name'),
        max_length=255,
        blank=False
    )
    description = models.TextField(
        _('Genre description'),
        blank=True
    )

    def __str__(self):
        return self.name


class Filmwork(IDMixin, TimeStampedMixin):
    '''
    Table, that stores films.
    '''

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('Filmwork')
        verbose_name_plural = _('Filmworks')
    
    title = models.TextField(
        _('Title'),
        blank=False
    )
    description = models.TextField(
        _('Filmwork description'),
        blank=True
    )
    creation_date = models.DateField(
        _('Premiere date')
    )
    rating = models.FloatField(
        _('Rating'),
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    type = models.CharField(
        _('Type'),
        choices=FilmType.choices
    )
    genres = models.ManyToManyField(
        'Genre', 
        through='GenreFilmWork'
    )
    persons = models.ManyToManyField(
        'Person',
        through='PersonFilmWork'
    )
    
    def __str__(self):
        return self.title


class GenreFilmwork(IDMixin):
    '''
    Secondary table, that connects `Genre` with `Filmwork`.
    '''

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = _('Genre filmwork')
        verbose_name_plural = _('Genres filmwork')
    
    film_work = models.ForeignKey(
        Filmwork, 
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        verbose_name=_('Filmwork genre'), 
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'''{self._meta.verbose_name} 
                    "{self.film_work.title}" - {self.genre.name}'''


class Person(IDMixin, TimeStampedMixin):
    '''
    Table, that stores persons.
    '''

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
    
    full_name = models.CharField(
        _('Person name'), 
        max_length=255,
        blank=False
    )
    
    def __str__(self):
        return self.full_name


class PersonFilmwork(IDMixin):
    '''
    Secondary table, that connects `Filmwork` with `Person`.
    '''

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = _('Filmwork participant')
        verbose_name_plural = _('Filmwork participants')
    
    film_work = models.ForeignKey(
        Filmwork, 
        on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Person,
        verbose_name=_('Participant'), 
        on_delete=models.CASCADE
    )
    role = models.TextField(
        _('Role'),
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return f'''{self._meta.verbose_name} 
                    "{self.film_work.title}" - {self.person.full_name}'''
