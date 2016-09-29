from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class CSVInput(models.Model):
    class Meta:
        db_table = 'csv_files'

    csv_file = models.FileField(upload_to="csv/")
    created_at = models.DateField(
        auto_now_add=True, editable=False
    )

    def __str__(self):

        return str(self.id)


class JournalEntry(models.Model):

    class Meta:
        db_table = 'journal_entries'

    journal_number = models.IntegerField()
    date = models.DateField()
    summary = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    currency = models.TextField(max_length=3)
    amount = models.FloatField()
    debit_credit = models.CharField(max_length=10)
    account_name = models.IntegerField()
    tax_code = models.CharField(max_length=255, null=True, blank=True)
    STATUS = (
        ('Successful', 'Successful'),
        ('Error', 'Error'),
    )
    status = models.CharField(max_length=11, choices=STATUS)
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    csv_input = models.ForeignKey(CSVInput)

