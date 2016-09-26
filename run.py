from SaasuAPI import SaasuAPI
from entity.Journal import Journal
from entity.JournalItem import JournalItem

""" webservices acess key"""
ws_access_key = "B6FEC20CDB084497B8773EA34056A23E"

""" file uid """
fileuid = "68914"

""" Need to update journal"""
uid_to_update = "81832338"

""" Instantiate SaasuAPI"""
saasu_api = SaasuAPI(ws_access_key, fileuid)

# to get entity_data
# entity_xml = saasu_api.get_entity('journal', uid)

# to get last updated uid of journal
# last_updated_uid = saasu_api.get_lastupdateduid('journal', uid)

""" Instantiate Journal Item and assign values"""
journal_item1 = JournalItem()
journal_item1.account_uid = "2673445"
journal_item1.tax_code = '0'
journal_item1.amount = "12.00"
journal_item1.card_type = 'Credit'

journal_item2 = JournalItem()
journal_item2.account_uid = "2673445"
journal_item2.tax_code = '0'
journal_item2.amount = "12.00"
journal_item2.card_type = 'Debit'

""" Create list of journal item list"""
journal_item_list = [journal_item1, journal_item2]

""" Instantiate Journal  and inject journal item
 instance with insert operation"""
journal = Journal(operation='insert', journal_items=journal_item_list)
journal.date = "2016/09/10"
journal.tags = "tags"
journal.summary = "journal2 "
journal.notes = "notes"
journal.requires_follow_up = "false"
journal.reference = "This is ref"

""" Will insert new journal journal """
saasu_api.save_entity(str(journal))


""" instantiate journal and inject journal item list with update operation"""
journal = Journal(operation='update', journal_items=journal_item_list)
journal.uid = uid_to_update

journal.last_update_uid = saasu_api.get_lastupdateduid(
    entity_name='journal',
    uid=journal.uid
)
journal.date = "2016/09/10"
journal.tags = "updates tags"
journal.summary = "update summary"
journal.notes = "update notes"
journal.requires_follow_up = "false"
journal.reference = "This is ref"

"""update journal with uid given """
saasu_api.save_entity(str(journal))
