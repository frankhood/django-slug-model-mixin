from django.db import models

from slug_model_mixin.model_mixins import SlugModelMixin


class ExampleModel(SlugModelMixin, models.Model):
    slugged_field = 'name'
    force_slugify = True

    name = models.CharField(
        'Name',
        max_length=255
    )

    class Meta:
        verbose_name = 'Example Model'
        verbose_name_plural = 'Example Models'


class ExampleSlugifyNotForcedModel(SlugModelMixin, models.Model):
    slugged_field = 'name'

    name = models.CharField(
        'Name',
        max_length=255
    )

    class Meta:
        verbose_name = 'Example slugify not forced Model'
        verbose_name_plural = 'Example slugify not forced Models'


class ExampleNotUniqueForcedModel(SlugModelMixin, models.Model):
    slugged_field = 'name'
    slug_unique = False
    force_slugify = True

    name = models.CharField(
        'Name',
        max_length=255
    )

    class Meta:
        verbose_name = 'Example not unique Model'
        verbose_name_plural = 'Example not unique Models'
