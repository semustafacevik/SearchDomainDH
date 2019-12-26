from Extensions.functions import *
import json
import grequests

class OTXSearch:

    def __init__(self, word):

        self.word = word
        self.results = ''
        self.t_result = ''
        self.total_results_ip = ''
        self.total_results_host = ''
        self.totalhosts = set()
        self.totalips = set()

    def do_search_otx(self):
        
        print("\nSearching OTX...")
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
            if(ip[0].isdigit()):
                self.total_results_ip += ip + " * "
        for host in self.totalhosts:
            self.total_results_host += host + " * "

        result['result_otx'] = self.total_results_host
        result_response['resultIPs'] = self.total_results_ip

        print('OK - OTX!')
