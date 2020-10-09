import uuid

from django.db import models

from django.utils.crypto import get_random_string


class SOURCE_TYPE(object):
    """Object class to represent Http request sources."""
    WEB = 1
    ANDROID = 2
    IOS = 3
    OTHER = 4

# Create your models here.


class BaseDjangoKtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    delete_flag = models.BooleanField(default=False)

    class Meta:
        abstract = True


class DjangoktSourceApiKeyModel(BaseDjangoKtModel):
    SOURCE_TYPE_CHOICES = (
        (SOURCE_TYPE.WEB, 'Web'),
        (SOURCE_TYPE.ANDROID, 'Android'),
        (SOURCE_TYPE.IOS, 'IOS'),
        (SOURCE_TYPE.OTHER, 'Other')
    )

    api_key = models.CharField(
        max_length=12,
        default=get_random_string,
        editable=False
    )
    app_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    source_type = models.PositiveIntegerField(choices=SOURCE_TYPE_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=False)
