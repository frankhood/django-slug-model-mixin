import factory.django

from tests.example.models import ExampleModel, ExampleSlugifyNotForcedModel, ExampleNotUniqueForcedModel


class ExampleModelFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = ExampleModel


class ExampleSlugifyNotForcedModelFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = ExampleSlugifyNotForcedModel


class ExampleNotUniqueForcedModelFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = ExampleNotUniqueForcedModel


