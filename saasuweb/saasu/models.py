from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


from django.db import models

# Create your models here.
from django.db import models
from .validators import FileValidator
# Create your models here.


class CSVInput(models.Model):

    class Meta:
        db_table = 'csv_files'

    csv_file = models.FileField(upload_to="csv/",
                                validators=[FileValidator(allowed_extensions=['csv']),
                                            FileValidator(max_size_=24*1024*1024)])
    # csv_file = models.FileField(upload_to="csv/", validators=[validate_file_extension])
    created_at = models.DateField(
        auto_now_add=True, editable=False
    )

    def __str__(self):

        return str(self.id)


class JournalEntry(models.Model):

    class Meta:
        db_table = 'journal_entries'

    data = JSONField(null=True, blank=True)

    STATUS = (
        ('Successful', 'Successful'),
        ('Error', 'Error'),
    )
    status = models.CharField(max_length=11, choices=STATUS)
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    csv_input = models.ForeignKey(CSVInput)

    def __str__(self):

        return "%s %s" % (str(self.created_at.date()), str(self.created_at.time()))

