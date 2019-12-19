from Extensions.functions import *
import json
import grequests

class OTXSearch:

    def __init__(self, word):

        self.word = word
        self.results = ''
        self.t_result = ''
        self.total_results = ''
        self.totalhosts = set()
        self.totalips = set()

    def do_search_otx(self):
        
        print("Searching OTX...")
        base_url = f'https://otx.alienvault.com/api/v1/indicators/domain/{self.word}/passive_dns'
        headers = {'User-Agent': get_user_agent()}
        try:
            request = grequests.get(base_url, headers=headers)
            data = grequests.map([request])
            self.results = data[0].content.decode('UTF-8')
        
        except Exception as e:
            print(e)

        self.t_result += self.results
        dct = json.loads(self.t_result)

        self.totalhosts: set = {host['hostname'] for host in dct['passive_dns']}
        self.totalips: set = {ip['address'] for ip in dct['passive_dns'] if 'NXDOMAIN' not in ip['address']}

        for ip in self.totalips:
            self.total_results += ip + " * "
        for host in self.totalhosts:
            self.total_results += host + " * "

        result['result_otx'] = self.total_results
        print('OK - OTX!')
