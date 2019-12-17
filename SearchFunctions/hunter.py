from Extensions.functions import *
import grequests

class HunterSearch:

    def __init__(self, word, limit):
        self.word = word
        self.limit = limit
        self.key = 'd7bc4b0dd5729e754fc7b883f116e9b3ba6da0e3'
        self.total_results = ''
        self.database = f'https://api.hunter.io/v2/domain-search?domain={self.word}&api_key={self.key}&limit={self.limit}'

    def do_search_hunter(self):
        
        print('Searching Hunter...')       
        request = grequests.get(self.database)
        response = grequests.map([request])
        self.total_results = response[0].content.decode('UTF-8')
        result['result_hunter'] = self.total_results
        print('OK - Hunter!')