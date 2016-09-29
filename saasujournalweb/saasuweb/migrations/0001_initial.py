# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVInput',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('csv_file', models.FileField(upload_to='csv/')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'csv_files',
            },
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('journal_number', models.IntegerField()),
                ('date', models.DateField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('currency', models.TextField(max_length=3)),
                ('amount', models.FloatField()),
                ('debit_credit', models.CharField(max_length=10)),
                ('account_name', models.IntegerField()),
                ('tax_code', models.CharField(blank=True, null=True, max_length=255)),
                ('status', models.CharField(choices=[('Successful', 'Successful'), ('Error', 'Error')], max_length=11)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('csv_input', models.ForeignKey(to='saasuweb.CSVInput')),
            ],
            options={
                'db_table': 'journal_entries',
            },
        ),
    ]
