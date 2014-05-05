# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting


class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('index'))
        self.assertStatusCode(200)

class PridetiZodiCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('prideti_zodi'))
        self.selectForm('#prideti-zodi-form')
        self.submitForm({
            'zodis': 'bandymas',
        })
        self.assertStatusCode(302)
        self.open(reverse('zodziai'))
        self.selectTable('#zodziai-table')
        self.assertTableHasRows("bandymas")
