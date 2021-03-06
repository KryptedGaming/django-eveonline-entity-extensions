from django.contrib.auth.models import User, Group
from django_eveonline_connector.models import EveCharacter, EveToken
from django.dispatch import receiver
from django.db.models.signals import m2m_changed, pre_delete, post_save
from django.db import transaction
from .tasks import update_eve_character_all
from django.core.exceptions import PermissionDenied

import logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=EveCharacter)
def user_token_update(sender, **kwargs):
    def call():
        evecharacter = kwargs.get('instance')
        if kwargs.get('created') and EveToken.objects.filter(evecharacter=evecharacter):
            update_eve_character_all.apply_async(args=[evecharacter.external_id])
    transaction.on_commit(call)