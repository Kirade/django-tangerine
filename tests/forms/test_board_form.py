from django.test import TestCase
from website.forms import BoardForm


class BoardFormTest(TestCase):

    def setUp(self):
        self.form = BoardForm()

    def test_form_label(self):
        """
        Test form label value
        """
        self.assertTrue(self.form.fields['title'].label == 'Title')
        self.assertTrue(self.form.fields['text'].label == 'Text')

