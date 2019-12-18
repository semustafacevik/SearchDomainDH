from Extensions.functions import *
import requests
 
class CertSpotterSearch:
 
    def __init__(self, word):
        
        self.word = word
        self.total_results = ''

    def do_search_certspotter(self):

        print('Searching CertSpotter...')
        base_url = f'https://api.certspotter.com/v1/issuances?domain={self.word}&include_subdomains=true&expand=dns_names&expand=issuer&expand=cert'
        headers = {'User-Agent': get_user_agent()}
        try:
            response = requests.get(base_url, headers=headers)
            self.total_results = response.text
        
        except Exception as e:
            print(e)

        result['result_certspotter'] = self.total_results
        print('OK - CertSpotter!')