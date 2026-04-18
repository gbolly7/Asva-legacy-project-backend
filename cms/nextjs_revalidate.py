from __future__ import annotations

import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def trigger_nextjs_revalidation(*, slug: str) -> None:
    """
    POST to Next.js on-demand revalidation when CMS content is published or updated while published.
    Expects Next route to accept JSON: {"secret": "...", "path": "..."} (common ISR pattern).
    """
    url = (getattr(settings, "NEXTJS_REVALIDATE_URL", None) or "").strip()
    secret = (getattr(settings, "NEXTJS_WEBHOOK_SECRET", None) or "").strip()
    if not url or not secret:
        logger.warning("Skipping Next.js revalidation: NEXTJS_REVALIDATE_URL or NEXTJS_WEBHOOK_SECRET is unset")
        return

    template = getattr(settings, "NEXTJS_REVALIDATE_PATH_TEMPLATE", "/{slug}")
    path = template.format(slug=slug)

    try:
        response = requests.post(
            url,
            json={"secret": secret, "path": path},
            timeout=10,
        )
        response.raise_for_status()
    except Exception:
        logger.exception("Next.js revalidation failed slug=%s path=%s", slug, path)
