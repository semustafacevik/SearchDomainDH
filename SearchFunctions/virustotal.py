from Extensions.functions import *
import requests


class VirusTotalSearch:

    def __init__(self, word):

        self.word = word
        self.results = ''
        self.total_results = ''

    def do_search_virustotal(self):

        print('Searching VirusTotal...')
        base_url = f'https://www.virustotal.com/ui/domains/{self.word}/subdomains?relationships=resolutions&cursor=STMwCi4%3D&limit=40'
        headers = {'User-Agent': get_user_agent()}
        res = requests.get(base_url, headers=headers)
        self.results = res.content.decode('UTF-8')
        self.total_results += self.results

        result['result_virustotal'] = self.total_results
        print('OK - VirusTotal!')