import uuid
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(
        _('description'),
        blank=True,
        null=True
    )

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('verbose_name_genre')
        verbose_name_plural = _('verbose_name_plural_genre')

    def __str__(self):
        return self.name


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(
        _('name'),
        max_length=255,
        blank=True
    )

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('verbose_name_person')
        verbose_name_plural = _('verbose_name_plural_person')

    def __str__(self):
        return self.full_name


class Filmwork(UUIDMixin, TimeStampedMixin):
    class FilmType(models.TextChoices):
        MOVIE = 'movie', _('movie')
        TV_SHOW = 'TV_SHOW', _('tv_show')

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    creation_date = models.DateField(_('creation_date'), blank=True, null=True)
    file_path = models.FileField(
        _('file_path'),
        blank=True,
        null=True,
        upload_to='movies/'
    )
    rating = models.FloatField(
        _('rating'),
        blank=True,
        null=True,
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)]
    )
    type = models.TextField(
        _('type'),
        blank=True,
        choices=FilmType.choices
    )
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')
    person = models.ManyToManyField(Person, through='PersonFilmwork')

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('verbose_name_film_work')
        verbose_name_plural = _('verbose_name_plural_film_work')
        indexes = [
            models.Index(fields=['creation_date'], name='film_work_creation_date_idx'),
        ]

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey(
        Filmwork,
        verbose_name=_('verbose_name_film_work'),
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        verbose_name=_('verbose_name_genre'),
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = _('verbose_name_genre_film_work')
        verbose_name_plural = _('verbose_name_plural_genre_film_work')
        constraints = [
            models.UniqueConstraint(fields=['film_work_id', 'genre_id'], name='film_work_genre_idx')
        ]


class PersonFilmwork(UUIDMixin):
    class RoleType(models.TextChoices):
        ACTOR = 'actor', _('actor')
        DIRECTOR = 'director', _('director')
        WRITER = 'writer', _('writer')

    film_work = models.ForeignKey(
        Filmwork,
        verbose_name=_('verbose_name_film_work'),
        on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Person,
        verbose_name=_('verbose_name_person'),
        on_delete=models.CASCADE
    )
    role = models.TextField(
        _('role'),
        null=True,
        choices=RoleType.choices
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = _('verbose_name_person_film_work')
        verbose_name_plural = _('verbose_name_plural_person_film_work')
        constraints = [
            models.UniqueConstraint(fields=['film_work_id', 'person_id', 'role'], name='film_work_person_idx')
        ]
