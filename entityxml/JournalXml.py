

class JournalXml:

    def __init__(self, operation):

        self.operation = operation

    def get_journal_xml(self):

        # xml = "{}"
        xml = '''<?xml version="1.0" encoding="utf-8"?>
                    <tasks
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
                        <{}Journal>'''.format(self.operation.lower())
        if self.operation == 'update':
            xml += '''<journal uid="{}" lastUpdatedUid="{}">'''
        elif self.operation == 'insert':
            xml += '''<journal uid="0">'''
        xml += '''<date>{}</date>
                    <tags>{}</tags>
                    <summary>{}</summary>
                    <notes>{}</notes>
                    <ccy>{}</ccy>
                    <autoPopulateFxRate>true</autoPopulateFxRate>
                    <requiresFollowUp>{}</requiresFollowUp>
                    <reference>{}</reference>
                    <journalItems>{}</journalItems>
                    </journal>
                '''

        xml += '''</{}Journal>
                    </tasks>'''.format(self.operation.lower())

        return xml

    def __str__(self):

        return self.get_journal_xml()
