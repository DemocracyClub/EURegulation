import csv
import re
import requests

from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from django.conf import settings

from regulations.models import Regulation, Summary


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.domain = "http://eur-lex.europa.eu"
        self.url_base = "{}/legal-content/en/LSU/".format(self.domain)

        self.HEADERS = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.37",
            "Accept-Language": "en-GB,en;q=0.8",
        }
        qs = Regulation.objects.filter(summaries=None).only('celex_number')
        for regulation in qs.iterator():
            url = "{}?uri=CELEX:{}".format(
                self.url_base,
                regulation.celex_number
            )
            print(url)
            summaries = self.get_summaries(url)
            for summary in summaries:
                regulation.summaries.add(summary)




    def get_summaries(self, url):
        print("Requesting")
        summaries = []
        req = requests.get(url, headers=self.HEADERS)
        if req.url.startswith(self.url_base):
            print("Seen a summary, grabbing it")
            # There is a summary for this
            soup = BeautifulSoup(req.text, "html5lib")
            codes = soup.find_all('a', href=re.compile('summary/EN/uriserv:'))
            if not codes:
                codes = soup.find_all('a', text="EN")

            print(codes)

            for code in codes:
                code = code['href'].split(':')[1]
                url = "{}/legal-content/EN/TXT/HTML/?uri=URISERV:{}".format(
                    self.domain, code)
                print(url)
                html_req = requests.get(url)
                summary_obj, _ = Summary.objects.update_or_create(
                    uri=url,
                    defaults={
                        'summary': html_req.text,
                    }
                )
                summaries.append(summary_obj)
        return summaries
