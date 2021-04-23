=====
Usage
=====

To use Django Slug Model Mixin in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_slug_model_mixin.apps.DjangoSlugModelMixinConfig',
        ...
    )

Add Django Slug Model Mixin's URL patterns:

.. code-block:: python

    from django_slug_model_mixin import urls as django_slug_model_mixin_urls


    urlpatterns = [
        ...
        url(r'^', include(django_slug_model_mixin_urls)),
        ...
    ]
