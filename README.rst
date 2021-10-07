=============================
Django Slug Model Mixin
=============================

.. image:: https://badge.fury.io/py/django-slug-model-mixin.svg?style=flat-square
    :target: https://badge.fury.io/py/django-slug-model-mixin

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest&style=flat-square
    :target: https://django-slug-model-mixin.readthedocs.io/en/latest/

.. image:: https://img.shields.io/coveralls/github/frankhood/django-slug-model-mixin/master?style=flat-square
    :target: https://coveralls.io/github/frankhood/django-slug-model-mixin?branch=master
    :alt: Coverage Status

Your project description goes here

Documentation
-------------

The full documentation is at https://django-slug-model-mixin.readthedocs.io.

Quickstart
----------

Install Django Slug Model Mixin::

    pip install django-slug-model-mixin

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
