import os
import csv

from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from django.conf import settings

from regulations.models import Regulation, Subject, Keyword


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(settings.BASE_DIR)
        file_path = os.path.join(
            settings.BASE_DIR, 'eu-legislation-subjects.csv')
        with open(file_path) as data_file:
            csv_file = csv.DictReader(data_file)
            for line in csv_file:
                self.process_line(line)

    def process_line(self, line):
        uuid = line['REG_CELLAR_ID'].split('/')[-1]

        try:
            reg = Regulation.objects.get(uuid=uuid)
        except Regulation.DoesNotExist:
            reg = self.add_new(uuid, line)

        subject, _ = Subject.objects.get_or_create(
            subject=line['REG_SUBJECT'])
        reg.subjects.add(subject)


    def add_new(self, uuid, line):
        print(uuid)
        reg = Regulation(
            uuid=uuid,
            uri=line['REG_URI'],
            year=line['REG_YEAR'],
            celex_number=line['REG_CELEX_NO'],
            number=line['REG_NUMBER'],
            title=line['REG_TITLE'],
        )

        content_path = os.path.join(
            settings.BASE_DIR,
            'docs',
            uuid[:2],
            "{}.html".format(uuid)

        )
        content_file = open(content_path)
        soup = BeautifulSoup(content_file, "html5lib")
        reg.body_html = soup.body.prettify()
        reg.body_text = soup.body.getText(separator='\n\n').replace('\n\n\n\n', '')

        def get_meta_tag_value(tag_name):
            tag = soup.find(attrs={'name': tag_name})
            if tag:
                return tag['content']
            else:
                return ""
        reg.DC_description = get_meta_tag_value('DC.description')
        reg.DC_identifier = get_meta_tag_value('DC.identifier')
        reg.DC_language = get_meta_tag_value('DC.language')
        reg.DC_publisher = get_meta_tag_value('DC.publisher')
        reg.DC_source = get_meta_tag_value('DC.source')
        reg.DC_title = get_meta_tag_value('DC.title')
        reg.DC_type = get_meta_tag_value('DC.type')
        reg.DC_subject = get_meta_tag_value('DC.subject')

        reg.save()

        keywords = reg.DC_subject.split(',')
        for keyword in keywords:
            keyword = keyword.strip()
            keyword = keyword.lower()
            if keyword:
                kw, _ = Keyword.objects.get_or_create(keyword=keyword)
                reg.keywords.add(kw)

        return reg

