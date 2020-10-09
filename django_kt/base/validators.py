from dateutil.relativedelta import relativedelta

from django.core.exceptions import ValidationError
from django.utils import timezone


def user_age_validator(date_obj, raise_exception=True):
    """Validator function to check if User is 18 years or older.

        Args:
            date_obj (object): Date object of User's Date of Birth.

        Returns:
            bool: True, if User is 18 years or older.

        Raises:
            ValidationError: If User is less than 18 years.
    """
    _today = timezone.now().date()

    if (date_obj + relativedelta(years=18)) > _today:
        days_difference = (_today - date_obj).days

        if raise_exception:
            raise ValidationError(
                'You are not old enough to trade, Please visit us after %s '
                'day(s).' % days_difference
            )

        return False

    return True
