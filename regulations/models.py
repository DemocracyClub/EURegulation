import re

from django.db import models
from django.db.models import Count
from django.core.urlresolvers import reverse

from bs4 import BeautifulSoup


class Regulation(models.Model):
    uuid = models.CharField(
        blank=True, max_length=255, db_index=True, unique=True)
    uri = models.CharField(blank=True, max_length=255, db_index=True)
    celex_number = models.CharField(blank=True, max_length=100)
    number = models.CharField(blank=True, max_length=100)
    year = models.IntegerField(blank=True, null=True)
    subjects = models.ManyToManyField('regulations.Subject')
    keywords = models.ManyToManyField('regulations.Keyword')
    title = models.TextField(blank=True)
    body_html = models.TextField(blank=True)
    body_text = models.TextField(blank=True)
    summaries = models.ManyToManyField('regulations.Summary')



    DC_description = models.TextField(blank=True)
    DC_identifier = models.TextField(blank=True)
    DC_language = models.TextField(blank=True)
    DC_publisher = models.TextField(blank=True)
    DC_source = models.TextField(blank=True)
    DC_subject = models.TextField(blank=True)
    DC_title = models.TextField(blank=True)
    DC_type = models.TextField(blank=True)

    def __str__(self):
        return "{} ({})".format(
            self.uuid,
            self.title
        )

    def clean_title(self):
        title = self.title
        # title = title.replace('\xa', ' ')
        title = title.replace('  ', ' ')

        title = re.sub(r"^Commission|Council|Implementing|Regulation[^\)]+\)", '', title).strip()

        title = re.sub(r"No [0-9]+/[0-9]+", '', title).strip()
        title = re.sub(r"[0-9]+/[0-9]+", '', title).strip()
        title = re.sub(r"of [0-9]+ [A-Za-z]+ [0-9]+", '', title).strip()
        title = re.sub(r"^amending", '', title).strip()
        title = re.sub(r"^of the Commission", '', title).strip()

        title = re.sub(r"^for the [0-9]+[rd|th]+ time", '', title).strip()

        if not title:
            title = self.title
        if len(title) > 0:
            title = title[0].upper() + title[1:]


        return title

    def get_absolute_url(self):
        return reverse("single_regulation_view", args=(self.year, self.celex_number))


    def html_text_only(self):
        soup = BeautifulSoup(self.body_html, "html5lib")
        return soup.find(id="TexteOnly")

    def text_for_search_index(self):
        text = ""
        for summary in self.summaries.all():
            soup = soup = BeautifulSoup(summary.summary, "html5lib")
            text = text + " " + soup.get_text()
        text = text + " " + self.body_text
        return " ".join(text.split(" ")[:2000])


class Summary(models.Model):
    uri = models.CharField(blank=True, max_length=1000)
    summary = models.TextField(blank=True)


class Subject(models.Model):
    subject = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.subject


class Keyword(models.Model):
    keyword = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.keyword

    def get_absolute_url(self):
        return reverse("single_keyword_view", args=(self.keyword,))

    def regulation_by_year(self):
        qs = self.regulation_set.all()
        qs = qs.values('year').annotate(total=Count('year')).order_by('year')
        return qs

