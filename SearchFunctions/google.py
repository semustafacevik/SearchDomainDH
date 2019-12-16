from Extensions.functions import *
import requests
import time
 
class GoogleSearch:
 
    def __init__(self, word, limit):
        
        self.word = word
        self.results_google = ''
        self.total_results_google = ''
        self.server = 'www.google.com'
        self.quantity = '100'
        self.limit = limit
        self.counter = 0

    def do_search_google(self):

        print('Searching Google...')
        while self.counter <= self.limit and self.counter <= 1000:
            urly = 'http://' + self.server + '/search?num=' + self.quantity + '&start=' + str(
                self.counter) + '&hl=en&meta=&q=%40\"' + self.word + '\"'
            try:
                headers = {'User-Agent': googleUA}
                response = requests.get(urly, headers=headers)
            except Exception as e:
                print(e)

            self.results_google = response.text

            if search(self.results_google):
                try:
                    self.results = google_workaround(urly)
                    if isinstance(self.results, bool):
                        print('Google is blocking your ip and the workaround, returning')
                        return
                except Exception:
                    # google blocked, no useful result
                    return

            time.sleep(getDelay())
            self.total_results_google += self.results_google
            self.counter += 100

        result['result_google'] = self.total_results_google
        print('OK - Google!')