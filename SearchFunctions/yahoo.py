from Extensions.functions import *
import grequests


class YahooSearch:
    def __init__(self, word, limit):
        self.word = word
        self.total_results_yahoo = ''
        self.server = 'search.yahoo.com'
        self.limit = limit

    def do_search_yahoo(self):
        print('Searching Yahoo...')
        base_url = f'https://{self.server}/search?p=%40{self.word}&b=xx&pz=100'
        headers = {
            'Host': self.server,
            'User-agent': get_user_agent()
            }
        urls = [base_url.replace("xx", str(num)) for num in range(
            0, self.limit, 100) if num <= self.limit]
        request = (grequests.get(url, headers=headers) for url in urls)
        responses = grequests.imap(request, size=5)
        for response in responses:
            self.total_results_yahoo += response.content.decode('UTF-8')

        result['result_yahoo'] = self.total_results_yahoo
        print('OK - Yahoo!')