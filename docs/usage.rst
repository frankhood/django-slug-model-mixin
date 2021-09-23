=====
Usage
=====

To use Django Slug Model Mixin in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'slug_model_mixin',
        ...
    )

Add Django Slug Model Mixin's URL patterns:

.. code-block:: python

    from slug_model_mixin import urls as slug_model_mixin_urls


    urlpatterns = [
        ...
        url(r'^', include(slug_model_mixin_urls)),
        ...
    ]
