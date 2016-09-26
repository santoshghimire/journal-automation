

class JournalItemXml:

    def __init__(self):
        self.journal_item = 'dsf'

        self.journal_item_list = []

    def get_journal_item_xml(self):

        xml = '''<journalItem>
                      <accountUid>{}</accountUid>
                      <taxCode>{}</taxCode>
                      <amount>{}</amount>
                      <type>{}</type>
                </journalItem>'''

        return xml

    def get_journal_item_list(self):

        return self.journal_item_list

    def __str__(self):

        return self.get_journal_item_xml()
