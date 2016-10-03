# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 09:48
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saasu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalentry',
            name='account_name',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='date',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='debit_credit',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='journal_number',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='tax_code',
        ),
        migrations.AddField(
            model_name='journalentry',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
