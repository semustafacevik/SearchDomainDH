from Extensions.functions import *
import grequests

class ThreatCrowdSearch:

    def __init__(self, word):

        self.word = word.replace(' ', '%20')
        self.results = ""
        self.total_results = ""

    def do_search_threatcrowd(self):
       
        print('\nSearching ThreatCrowd...')
        base_url = f'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={self.word}'
        headers = {'User-Agent': get_user_agent()}
        try:
            request = grequests.get(base_url, headers=headers)
            data = grequests.map([request])
            self.results = data[0].content.decode('UTF-8')
        except Exception as e:
            print(e)
        self.total_results += self.results

        result['result_threatcrowd'] = self.total_results
        print('OK - ThreatCrowd!')