from Extensions.functions import *
import requests
import time

class LinkedInSearch:

    def __init__(self, word, limit):
        
        self.word = word.replace(' ', '%20')
        self.results = ''
        self.total_results = ''
        self.server = 'www.google.com'
        self.limit = limit
        self.counter = 0

    def do_search_linkedin(self):

        print('\nSearching LinkedIn...')
        result['result_linkedin'] = ''
        while self.counter <= self.limit and self.counter <= 1000:
            urly = 'http://' + self.server + '/search?num=100&start=' + str(self.counter) + '&hl=en&meta=&q=site%3Alinkedin.com/in%20' + self.word
            try:
                headers = {'User-Agent': get_user_agent()}
                response = requests.get(urly, headers=headers)
                
            except Exception as e:
                print(e)
                break
            
            self.results = response.text
           
            if search(self.results):
                print('Google blocked, no useful result.')
                break

            time.sleep(getDelay())
            self.total_results += self.results
            self.counter += 100
                   
        result['result_linkedin'] = self.total_results
        print('OK - LinkedIn!')
