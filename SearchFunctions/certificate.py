from Extensions.functions import *
import requests
 
class CertificateSearch:
 
    def __init__(self, word):
        
        self.word = word
        self.total_results = ''

    def do_search_certificate(self):

        print('Searching Certificate...')
        base_url = f'https://crt.sh/?q=%25.{self.word}&output=json'
        headers = {'User-Agent': get_user_agent()}
        try:
            response = requests.get(base_url, headers=headers)
            self.total_results = response.text
        
        except Exception as e:
            print(e)

        result['result_certificate'] = self.total_results
        print('OK - Certificate!')