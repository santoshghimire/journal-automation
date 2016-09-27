from entityxml.JournalXml import JournalXml


class Journal:

    def __init__(self, operation, journal_items=None):

        self.operation = operation
        self.journal_xml = JournalXml(self.operation)
        self.uid = None
        self.last_update_uid = None
        self.date = None
        self.tags = None
        self.summary = None
        self.notes = None
        self.requires_follow_up = False
        self.journal_items = [str(x) for x in journal_items]
        self.journal_items = "\n".join(self.journal_items)
        self.currency = '41'
        self.auto_populate_fx_rate = False,
        self.fc_to_bc_fx_rate = None,
        self.reference = None

    def get_uid(self):
        return self.uid

    def get_last_update_uid(self):
        return self.last_update_uid

    def get_summary(self):
        return self.summary

    def get_tags(self):
        return self.tags

    def get_requires_follow_up(self):
        return self.requires_follow_up

    def get_journal_items(self):
        return self.journal_items

    def get_currency(self):
        return self.currency

    def get_auto_populate_fx_rate(self):
        return self.auto_populate_fx_rate

    def get_fc_to_bc_fx_rate(self):
        return self.fc_to_bc_fx_rate

    def get_reference(self):
        return self.reference

    def __str__(self):
        if self.operation == 'insert':

            return str(self.journal_xml).format(
                self.date, self.tags, self.summary,
                self.notes, self.currency, self.requires_follow_up,
                self.reference, self.journal_items
            )
        if self.operation == 'update':
            return str(self.journal_xml).format(
                self.uid, self.last_update_uid,
                self.date, self.tags, self.summary,
                self.notes, self.currency,  self.requires_follow_up,
                self.reference, self.journal_items,
            )
