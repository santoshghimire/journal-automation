
from ..entityxml.JournalItemXml import JournalItemXml


class JournalItem:

    def __init__(self):
        self.journal_item_xml = JournalItemXml()
        self.account_uid = ""
        self.tax_code = ""
        self.amount = ""
        self.card_type = ""

    def get_account_uid(self):
        return self.account_uid

    def get_tax_code(self):
        return self.tax_code

    def get_amount(self):
        return self.amount

    def get_card_type(self):
        return self.card_type

    def __str__(self):

        return str(self.journal_item_xml).format(
            self.account_uid, self.tax_code,
            self.amount, self.card_type,
         )
