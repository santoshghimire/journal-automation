from SaasuAPI import SaasuAPI
from entity.Journal import Journal
from entity.JournalItem import JournalItem

import json

with open('settings/api_config.json') as api_connection_data:
    api_connection_data = json.load(api_connection_data)

print (api_connection_data['ws_access_key'])
print (api_connection_data['file_uid'][0])

# """ webservices acess key"""
ws_access_key = api_connection_data['ws_access_key']

""" file uid """
file_uid = api_connection_data['file_uid'][0]

""" Need to update journal"""
# uid_to_update = "81832338"
uid_to_update = "81858581"

""" Instantiate SaasuAPI"""
saasu_api = SaasuAPI(ws_access_key, file_uid)

# to get entity_data
# entity_xml = saasu_api.get_entity('journal', uid)

# to get last updated uid of journal
# last_updated_uid = saasu_api.get_lastupdateduid('journal', uid)

""" Instantiate Journal Item and assign values"""
journal_item1 = JournalItem()
# journal_item1.account_uid = "2673445"
journal_item1.account_uid = "2674400"
journal_item1.tax_code = '0'
journal_item1.amount = "12.00"
journal_item1.card_type = 'Credit'

journal_item2 = JournalItem()
journal_item2.account_uid = "2674400"
journal_item2.tax_code = '0'
journal_item2.amount = "12.00"
journal_item2.card_type = 'Debit'

""" Create list of journal item list"""
journal_item_list = [journal_item1, journal_item2]

""" Instantiate Journal  and inject journal item
 instance with insert operation"""
journal = Journal(operation='insert', journal_items=journal_item_list)
journal.date = "2016/09/27"
journal.tags = "tags"
journal.summary = "journal 2"
journal.notes = "notes"
journal.requires_follow_up = "false"
journal.reference = "This is ref"
journal.currency ="NZD"


""" Will insert new journal journal """
saasu_api.save_entity(str(journal))


""" instantiate journal and inject journal item list with update operation"""
journal = Journal(operation='update', journal_items=journal_item_list)
journal.uid = uid_to_update

journal.last_update_uid = saasu_api.get_lastupdateduid(
    entity_name='journal',
    uid=journal.uid
)
journal.date = "2016/09/26"
journal.tags = "updates tags"
journal.summary = "update summary 111"
journal.notes = "update notes"
journal.requires_follow_up = "false"
journal.reference = "This is ref updated"
journal.currency = "NZD"


"""update journal with uid given """
saasu_api.save_entity(str(journal))
