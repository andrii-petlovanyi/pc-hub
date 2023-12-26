import os
from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv('DJANGO_ENV')

if ENVIRONMENT == 'prod':
    from .prod import *
else:
    from .dev import *