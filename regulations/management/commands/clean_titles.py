import csv
import re
import requests

from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from django.conf import settings

from regulations.models import Regulation


class Command(BaseCommand):

    def handle(self, *args, **options):
        qs = Regulation.objects.all().only('title')
        for regulation in qs:
            print()
            print(repr(regulation.clean_title()))
            print()

