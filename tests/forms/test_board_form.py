from django.test import TestCase
from website.forms import BoardForm


class BoardFormTest(TestCase):

    def setUp(self):
        self.form = BoardForm()

    def test_title_label(self):
        self.assertTrue(self.form.fields['title'].label == 'Title')

    def test_text_label(self):
        self.assertTrue(self.form.fields['text'].label == 'Text')
