import csv
from .SaasuAPI import SaasuAPI
from .entity.Journal import Journal
from .entity.JournalItem import JournalItem
from saasu.models import JournalEntry
import json


class CSVReader:

    def __init__(self, csv_path, csv_object):


        with open('settings/api_config.json') as api_connection_data:
            api_connection_data = json.load(api_connection_data)

        with open('settings/account_settings.json') as account_settings:
            self.account_settings = json.load(account_settings)

        # """ webservices acess key"""
        ws_access_key = api_connection_data['ws_access_key']

        """ file uid """
        file_uid = api_connection_data['file_uid'][0]

        """ Instantiate SaasuAPI"""
        self.saasu_api = SaasuAPI(ws_access_key, file_uid)

        self.csv_path = csv_path
        self.csv_object = csv_object

        self.journal_dict = self.create_journal_dict()

        # print journal_dict




    def create_journal_dict(self):

        with open(self.csv_path) as csvfile:

            journal = csv.DictReader(csvfile)
            journal_dict = {}
            journal_number_list = []
            for row in journal:
                journal_number = row['journal_number']

                if journal_number not in journal_number_list:
                    journal_number_list.append(journal_number)
                    journal_dict.update({

                        journal_number: {
                            'journal': {
                                'date': row['date'],
                                'summary': row['summary'],
                                'tags': row['tags'],
                                'currency': row['currency']
                            },
                            'journal_items': [{
                                'account_name': row['account_name'],
                                'tax_code': row['tax_code'],
                                'card_type': row['debit/credit'],
                                'amount': row['amount'],
                            }]
                        }

                    })
                else:
                    journal_dict[journal_number]['journal_items'].append({
                        'account_name': row['account_name'],
                        'tax_code': row['tax_code'],
                        'card_type': row['debit/credit'],
                        'amount': row['amount']
                    })

        return journal_dict

    def get_journal_and_insert(self):
        journal_dict = self.journal_dict

        status_list =[]
        for journal_number in journal_dict:
            journal_items_object_list = []

            for item in journal_dict[journal_number]['journal_items']:
                journal_item = JournalItem()
                journal_item.card_type = item['card_type']
                journal_item.tax_code = item['tax_code']
                journal_item.amount = float(item['amount'])
                try:
                    journal_item.account_uid = self.account_settings[
                        item['account_name']
                    ]
                except:
                    print("*"*40)
                    account_error = "ERROR !! Account [{}] for Journal number [{}] "
                    "not exist in account settings".format(
                        item['account_name'], journal_number)

                    print("ERROR !! Account [{}] for Journal number [{}] "
                          "not exist in account settings".format(
                            item['account_name'], journal_number))
                    print("*"*40)
                    status_list.append({"status": "Error", "remarks": account_error})

                journal_items_object_list.append(journal_item)

            journal = Journal(operation='insert',
                              journal_items=journal_items_object_list)

            journal.date = journal_dict[journal_number]['journal']['date']
            journal.tags = journal_dict[journal_number]['journal']['tags']
            journal.summary = journal_dict[journal_number]['journal']['summary']
            journal.currency = journal_dict[journal_number]['journal']['currency']


            status, remarks = self.saasu_api.save_entity(str(journal), journal_number)

            JournalEntry.objects.create(
                csv_input=self.csv_object,
                data=journal_dict,
                status=status,
                remarks=remarks
            )

            status_list.append({
                "status": status,
                "remarks": remarks
            })

        return status_list





