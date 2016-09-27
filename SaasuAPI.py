import urllib
import urllib2
import requests
from bs4 import BeautifulSoup


class SaasuAPI:

    api_base_url = 'https://secure.saasu.com/webservices/rest/r1/'

    def __init__(self, ws_access_key, file_uid):
        self.web_services_url = SaasuAPI.api_base_url
        self.ws_access_key = ws_access_key
        self.file_uid = file_uid
        self.url_dict_param = {'wsaccesskey': self.ws_access_key,
                               'fileuid': self.file_uid}

    def build_api_url(self, base_url, url_dict_param=None):
        if not url_dict_param:
            url_dict_param = self.url_dict_param
        return "{}?{}".format(base_url, urllib.urlencode(url_dict_param))

    def save_entity(self, entity_xml_data, journal_number):
        url = self.build_api_url('Tasks', url_dict_param=None)
        api_connection_url = "{}{}".format(self.web_services_url, url)

        # set what your server accepts
        headers = {'Content-Type': 'application/xml'}

        response = requests.post(api_connection_url,
                                 data=entity_xml_data,
                                 headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')
        message = ""

        if '<errors>' in response.text:
                error_msg = soup.message.text
                message = "Journal Number :[{}] INSERT FAILED : {}!!".format(
                    journal_number, error_msg)
        else:
            message = " Journal Number :[{}] INSERT SUCCESSFUL !!".format(
                journal_number)
        print message

    def get_entity(self, entity_name, uid):
        entity_name = entity_name.lower().title()
        self.url_dict_param.update({'uid': uid})
        url = self.build_api_url(entity_name, self.url_dict_param)
        api_connection_url = "{}{}".format(self.web_services_url, url)

        return urllib2.urlopen(api_connection_url).read()

    def get_lastupdateduid(self, entity_name, uid):

        entity_xml_data = self.get_entity(entity_name, uid)
        soup = BeautifulSoup(entity_xml_data, 'lxml')

        journal_tag = soup.journal
        last_updated_uid = journal_tag['lastupdateduid']
        return last_updated_uid
