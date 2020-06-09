from django.test import TestCase
import datetime
from django.utils import timezone
from catalog.forms import RenewBookForm

class RenewBookFormTest(TestCase):
	def test_renew_form_date_field_label(self):
		from = RenewBookForm()
		self.assertTrue(form.fields['renewal_date'].label == None or form.field['renewal_date'] == 'renewal_date')
