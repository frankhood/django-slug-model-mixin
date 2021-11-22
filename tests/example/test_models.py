#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-slug-model-mixin
------------

Tests for `django-slug-model-mixin` models module.
"""
from django.test import TestCase
from django.utils.text import slugify

from tests.example.factories import ExampleModelFactory


class TestDjangoSlugModelMixin(TestCase):
    def test_slug_creation(self):
        example = ExampleModelFactory()
        self.assertEqual(example.slug, slugify(example.name))

    def test_same_name_slug_unique_uuslug(self):
        example_one = ExampleModelFactory(name="Test")
        example_two = ExampleModelFactory(name="Test")
        example_three = ExampleModelFactory(name="Test")
        self.assertEqual(example_one.slug, "test")
        self.assertNotEqual(example_one.slug, example_two.slug)
        self.assertNotEqual(example_one.slug, example_three.slug)
        self.assertNotEqual(example_two.slug, example_three.slug)

    def test_same_name_slug_unique_no_uuslug(self):
        # with mock.patch.dict(sys.modules, {'uuslug': None}):
        #     with mock.patch.dict(sys.modules, {'uuslug.uuslug': None}):
        # sys.modules['uuslug'] = None
        # sys.modules['uuslug.uuslug'] = None
        example_one = ExampleModelFactory(name="Test")
        example_two = ExampleModelFactory(name="Test")
        example_three = ExampleModelFactory(name="Test")
        self.assertEqual(example_one.slug, "test")
        self.assertNotEqual(example_one.slug, example_two.slug)
        self.assertNotEqual(example_one.slug, example_three.slug)
        self.assertNotEqual(example_two.slug, example_three.slug)

    def test_example_with_same_slug_not_already_created_forced(self):
        example_one = ExampleModelFactory(name="Test")
        self.assertEqual(example_one.slug, "test")
        example_two = ExampleModelFactory(name="Test", slug="test")
        self.assertNotEqual(example_one.slug, example_two.slug)

    def test_example_with_same_slug_already_created_forced(self):
        example_one = ExampleModelFactory(name="Test")
        example_two = ExampleModelFactory(name="Test")
        self.assertEqual(example_one.slug, "test")
        self.assertNotEqual(example_one.slug, example_two.slug)
        example_two.slug = "test"
        example_two.save()
        self.assertNotEqual(example_two.slug, "test")
        self.assertEqual(example_two.slug, "test-1")

    def test_example_with_same_slug_and_with_spaces(self):
        example_one = ExampleModelFactory(name="Test One")
        self.assertEqual(example_one.slug, "test-one")
        example_two = ExampleModelFactory(name="Test One", slug="test-one")
        self.assertNotEqual(example_one.slug, example_two.slug)
        self.assertEqual(example_two.slug, "test-one-1")
