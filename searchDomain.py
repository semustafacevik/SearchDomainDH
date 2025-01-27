from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from datetime import datetime
from Extensions.functions import *
from Extensions.regexs import * 
from SearchFunctions import *

app = Flask(__name__)
api = Api(app)

class SearchWordFree(Resource):
    def get(self, word):

        result_response['searchQuery'] = word
        result_response['searchDate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        from requests import get
        result_response['searchIP'] = get('https://api.ipify.org').text

        from SearchFunctions import bing
        searchBing = bing.BingSearch(word, 50)
        searchBing.do_search_bing()

        from SearchFunctions import google
        searchGoogle = google.GoogleSearch(word, 20)
        searchGoogle.do_search_google()

        from SearchFunctions import yahoo
        searchYahoo = yahoo.YahooSearch(word, 50)
        searchYahoo.do_search_yahoo()

        regex = Regexs(word)
        regex.getEmails()

        print("\n****  FINISHED!  ****\n")
             
        return result_response

class SearchWordMember(Resource):

    def get(self, word):

        result_response['searchQuery'] = word
        result_response['searchDate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        from requests import get
        result_response['searchIP'] = get('https://api.ipify.org').text

        from SearchFunctions import bing
        searchBing = bing.BingSearch(word, 200)
        searchBing.do_search_bing()

        from SearchFunctions import certificate
        searchCertificate = certificate.CertificateSearch(word)
        searchCertificate.do_search_certificate()
        
        from SearchFunctions import certspotter
        searchCertSpotter = certspotter.CertSpotterSearch(word)
        searchCertSpotter.do_search_certspotter()

        from SearchFunctions import google
        searchGoogle = google.GoogleSearch(word, 90)
        searchGoogle.do_search_google()

        from SearchFunctions import linkedin
        searchLinkedIn = linkedin.LinkedInSearch(word, 90)
        searchLinkedIn.do_search_linkedin()

        from SearchFunctions import otx
        searchOTX = otx.OTXSearch(word)
        searchOTX.do_search_otx()

        from SearchFunctions import portscanner
        searchPortScan = portscanner.PortScanSearch(word)
        searchPortScan.do_search_portscan()

        from SearchFunctions import threatcrowd
        searchThreatCrowd = threatcrowd.ThreatCrowdSearch(word)
        searchThreatCrowd.do_search_threatcrowd()

        from SearchFunctions import virustotal
        searchVirusTotal = virustotal.VirusTotalSearch(word)
        searchVirusTotal.do_search_virustotal()

        from SearchFunctions import yahoo
        searchYahoo = yahoo.YahooSearch(word, 200)
        searchYahoo.do_search_yahoo()

        rgx = Regexs(word)
        rgx.getEmails()
        rgx.getFileUrls()
        rgx.getHostnames()
        rgx.getLinkedInLinks()
        rgx.getLinkedInProfiles()

        print("\n****  FINISHED!  ****\n")
             
        return result_response

api.add_resource(SearchWordFree, '/search/<word>')
api.add_resource(SearchWordMember, '/membersearch/<word>')

if __name__ == '__main__':
    app.run(debug=True)