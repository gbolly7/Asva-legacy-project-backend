from __future__ import annotations

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Content
from .nextjs_revalidate import trigger_nextjs_revalidation


@receiver(post_save, sender=Content)
def revalidate_nextjs_on_published_content(sender, instance: Content, **kwargs) -> None:
    if instance.status != Content.Status.PUBLISHED:
        return
    trigger_nextjs_revalidation(slug=instance.slug)
