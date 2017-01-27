from django.db import models

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


class Subject(models.Model):
    subject = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.subject


class Keyword(models.Model):
    keyword = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.keyword
