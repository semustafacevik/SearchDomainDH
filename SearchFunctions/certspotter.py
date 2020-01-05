from Extensions.functions import *
import requests
 
class CertSpotterSearch:
 
    def __init__(self, word):
        
        self.word = word
        self.total_results = ''
        self.total_hosts = set()

    def do_search_certspotter(self):

        print('\nSearching CertSpotter...')

        base_url = f'https://api.certspotter.com/v1/issuances?domain={self.word}&include_subdomains=true&expand=dns_names&expand=issuer&expand=cert'
        headers = {'User-Agent': get_user_agent()}
        try:
            request = requests.get(base_url, headers=headers)
            response = request.json()
            for dct in response:
                for key, value in dct.items():
                    if key == 'dns_names':
                        self.total_hosts.update({name for name in value if name})

            for hostname in self.total_hosts:
                self.total_results += '¨' + hostname

            result['result_certspotter'] = self.total_results         

        except Exception as e:
            print(e)

        print('OK - CertSpotter!')