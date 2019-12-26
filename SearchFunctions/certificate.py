from Extensions.functions import *
import requests
 
class CertificateSearch:
 
    def __init__(self, word):
        
        self.word = word
        self.total_results = ''

    def do_search_certificate(self):

        print('\nSearcing Certifacate...')
        hostnames = set()
        url = f'https://crt.sh/?q=%25.{self.word}&output=json'
        headers = {'User-Agent': get_user_agent()}
        request = requests.get(url, headers=headers, timeout=5)
        if request.ok:
            response = request.json()
            hostnames = set([dct['name_value'][2:] if '*.' == dct['name_value'][:2] else dct['name_value'] for dct in response])

        for hostname in hostnames:
            self.total_results += hostname + " * "

        result['result_certificate'] = self.total_results
        print('OK - Certificate!')