"""
ASGI config for ecommerce project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from pathlib import pathlib
from dotenv import load_dotenv

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

application = get_asgi_application()
