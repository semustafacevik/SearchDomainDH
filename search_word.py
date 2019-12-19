from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from Extensions.functions import *
from SearchFunctions import *

app = Flask(__name__)
api = Api(app)

class SearchWordFree(Resource):

    def get(self, word):

        from SearchFunctions import virustotal
        searchVirusTotal = virustotal.VirusTotalSearch(word)
        searchVirusTotal.do_search_virustotal()

        # from SearchFunctions import certspotter
        # searchCertSpotter = certspotter.CertSpotterSearch(word)
        # searchCertSpotter.do_search_certspotter()

        # from SearchFunctions import certificate
        # searchCertificate = certificate.CertificateSearch(word)
        # searchCertificate.do_search_certificate()

        # from SearchFunctions import linkedin
        # searchLinkedIn = linkedin.LinkedInSearch(word, 100)
        # searchLinkedIn.do_search_linkedin()


    ######################3
        # from SearchFunctions import bing
        # searchBing = bing.BingSearch(word, 50)
        # searchBing.do_search_bing()

        # from SearchFunctions import google
        # searchGoogle = google.GoogleSearch(word, 20)
        # searchGoogle.do_search_google()

        # from SearchFunctions import yahoo
        # searchYahoo = yahoo.YahooSearch(word, 50)
        # searchYahoo.do_search_yahoo()
        
        return result


class SearchWordMember(Resource):

    def get(self, word):
        
        from SearchFunctions import bing
        searchBing = bing.BingSearch(word, 500)
        searchBing.do_search_bing()

        # from SearchFunctions import google
        # searchGoogle = google.GoogleSearch(word, 500)
        # searchGoogle.do_search_google()

        # from SearchFunctions import hunter
        # searchHunter = hunter.HunterSearch(word,100)
        # searchHunter.do_search_hunter()

        from SearchFunctions import yahoo
        searchYahoo = yahoo.YahooSearch(word, 500)
        searchYahoo.do_search_yahoo()

        return result


api.add_resource(SearchWordFree, '/search/<word>')
api.add_resource(SearchWordMember, '/membersearch/<word>')

if __name__ == '__main__':
    app.run(debug=True)