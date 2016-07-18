# import from python standard module
import datetime

# import from django
from django.utils import timezone
from django.test import TestCase

# import from app
from .models import Achievements


class CommonInfoMethodTests(TestCase):

    def test_is_date_validate_with_to_date_set_to_future(self):
        # is_date_validate() should return False if to_data is set to future.

        now = timezone.now()
        delta = datetime.timedelta(days=100)
        to_date_future = Achievements(to_date=now + delta, from_date=now - delta)
        self.assertEqual(to_date_future.is_date_validate(), False)

    def test_is_date_validate_with_from_date_set_to_future(self):
        # is_date_validate() should return False if from_data is set to future.

        now = timezone.now()
        delta = datetime.timedelta(days=100)
        from_date_future = Achievements(from_date=now + delta, to_date=now - delta)
        self.assertEqual(from_date_future.is_date_validate(), False)

    def test_is_date_validate_with_to_date_after_from_date(self):
        # is_date_validate() should return False if to_date < from_date.

        now = timezone.now()
        delta = datetime.timedelta(days=10)
        date_faulty = Achievements(from_date=now - delta * 5, to_date=now - delta * 10)
        self.assertEqual(date_faulty.is_date_validate(), False)




