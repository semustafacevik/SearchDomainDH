from Extensions.functions import *
import grequests

class BingSearch:
    def __init__(self, word, limit):

        self.word = word.replace(' ', '%20')
        self.total_results = ''
        self.server = 'www.bing.com'
        self.limit = limit

    def do_search_bing(self):
        
        print('\n****  Searching ' + self.word + '  ****')
        print('\nSearcing Bing...')
        headers = {
            'Host': self.server,
            'Cookie': 'SRCHHPGUSR=ADLT=DEMOTE&NRSLT=50',
            'Accept-Language': 'en-us,en',
            'User-agent': get_user_agent()
        }
        base_url = f'https://{self.server}/search?q=%40{self.word}&count=100&first=xx'
        urls = [base_url.replace("xx", str(num)) for num in range(
            0, self.limit, 100) if num <= self.limit]
        request = (grequests.get(url, headers=headers, timeout=5)for url in urls)
        responses = grequests.imap(request, size=5)
        for response in responses:
            self.total_results += response.content.decode('UTF-8')
        
        result['result_bing'] = self.total_results
        print('OK - Bing!')