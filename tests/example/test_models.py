#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
django-slug-model-mixin
------------

Tests for `slug-model-mixin` models module.
"""

import sys

import mock
from django.test import TestCase
from django.utils.text import slugify
from freezegun import freeze_time

from tests.example.factories import (
    ExampleModelFactory,
    ExampleSlugifyNotForcedModelFactory,
    ExampleNotUniqueForcedModelFactory
)


class TestDjangoSlugModelMixin(TestCase):

    def test_slug_creation(self):
        with self.subTest('force_slugify True'):
            example = ExampleModelFactory()
            self.assertEqual(example.slug, slugify(example.name))

        with self.subTest('force_slugify False'):
            example = ExampleSlugifyNotForcedModelFactory()
            self.assertEqual(example.slug, '')

        with self.subTest('slug_unique False'):
            example_one = ExampleNotUniqueForcedModelFactory(name='Test')
            example_two = ExampleNotUniqueForcedModelFactory(name='Test')
            self.assertEqual(example_one.slug, example_two.slug)

    def test_same_name_slug_unique_uuslug(self):
        example_one = ExampleModelFactory(name='Test')
        example_two = ExampleModelFactory(name='Test')
        example_three = ExampleModelFactory(name='Test')
        self.assertEqual(example_one.slug, 'test')
        self.assertNotEqual(example_one.slug, example_two.slug)
        self.assertNotEqual(example_one.slug, example_three.slug)
        self.assertNotEqual(example_two.slug, example_three.slug)

    def test_same_name_slug_unique_no_uuslug(self):
        # with mock.patch.dict(sys.modules, {'uuslug': None}):
        #     with mock.patch.dict(sys.modules, {'uuslug.uuslug': None}):
        # sys.modules['uuslug'] = None
        # sys.modules['uuslug.uuslug'] = None
        example_one = ExampleModelFactory(name='Test')
        example_two = ExampleModelFactory(name='Test')
        example_three = ExampleModelFactory(name='Test')
        self.assertEqual(example_one.slug, 'test')
        self.assertNotEqual(example_one.slug, example_two.slug)
        self.assertNotEqual(example_one.slug, example_three.slug)
        self.assertNotEqual(example_two.slug, example_three.slug)

    def test_example_with_same_slug_not_already_created_forced(self):
        example_one = ExampleModelFactory(name='Test')
        self.assertEqual(example_one.slug, 'test')
        example_two = ExampleModelFactory(name='Test', slug='test')
        self.assertNotEqual(example_one.slug, example_two.slug)

    def test_example_with_same_slug_already_created_forced(self):
        example_one = ExampleModelFactory(name='Test')
        example_two = ExampleModelFactory(name='Test')
        self.assertEqual(example_one.slug, 'test')
        self.assertNotEqual(example_one.slug, example_two.slug)
        example_two.slug = 'test'
        example_two.save()
        self.assertNotEqual(example_two.slug, 'test')
        self.assertEqual(example_two.slug, '{}-{}'.format(
            slugify(example_two.name),
            example_two.id
        ))
        self.assertEqual(example_two.slug, 'test-2')

    @freeze_time('10-10-2020')
    def test_example_with_same_slug_already_created_with_same_id_forced(self):
        example_one = ExampleModelFactory(name='Test')
        example_two = ExampleModelFactory(name='Test')
        example_three = ExampleModelFactory(name='Test', slug='test-2')
        self.assertEqual(example_one.slug, 'test')
        self.assertEqual(example_three.slug, 'test-2')
        self.assertNotEqual(example_one.slug, example_two.slug)
        example_two.slug = 'test'
        example_two.save()
        self.assertNotEqual(example_two.slug, 'test')
        self.assertNotEqual(example_two.slug, '{}-{}'.format(
            slugify(example_two.name),
            example_two.id
        ))
        self.assertNotEqual(example_two.slug, 'test-2')

    def tearDown(self):
        pass
