import os
from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv('DJANGO_ENV')
print(ENVIRONMENT)

if ENVIRONMENT == 'prod':
    from .prod import *
else:
    from .dev import *