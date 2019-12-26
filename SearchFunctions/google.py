from Extensions.functions import *
import requests
import time
 
class GoogleSearch:
 
    def __init__(self, word, limit):
        
        self.word = word
        self.results = ''
        self.total_results = ''
        self.server = 'www.google.com'
        self.limit = limit
        self.counter = 0

    def do_search_google(self):

        print('\nSearching Google...')
        while self.counter <= self.limit and self.counter <= 1000:
            urly = 'http://' + self.server + '/search?num=100&start=' + str(self.counter) + '&hl=en&meta=&q=%40' + self.word
            try:
                headers = {'User-Agent': get_user_agent()}
                response = requests.get(urly, headers=headers)
            except Exception as e:
                print(e)

            self.results = response.text

            if search(self.results):
                print('Google is blocking your ip and the workaround, returning.')
                return
                
            time.sleep(getDelay())
            self.total_results += self.results
            self.counter += 100

        result['result_google'] = self.total_results
        print('OK - Google!')