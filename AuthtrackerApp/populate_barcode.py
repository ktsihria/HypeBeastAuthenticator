import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ClothingAuthTracker.settings')

import django
django.setup()

import random
from AuthtrackerApp.models import Barcode
