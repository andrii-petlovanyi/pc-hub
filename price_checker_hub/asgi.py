"""
ASGI config for price_checker_hub project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from .routing import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_checker_hub.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
    }
)
