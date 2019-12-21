from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from Extensions.functions import *
from Extensions.regexs import * 
from SearchFunctions import *

app = Flask(__name__)
api = Api(app)

class SearchWordFree(Resource):

    def get(self, word):

        from SearchFunctions import bing
        searchBing = bing.BingSearch(word, 100)
        searchBing.do_search_bing()

        # from SearchFunctions import certificate
        # searchCertificate = certificate.CertificateSearch(word)
        # searchCertificate.do_search_certificate()
        
        # from SearchFunctions import certspotter
        # searchCertSpotter = certspotter.CertSpotterSearch(word)
        # searchCertSpotter.do_search_certspotter()

        from SearchFunctions import google
        searchGoogle = google.GoogleSearch(word, 100)
        searchGoogle.do_search_google()

        from SearchFunctions import linkedin
        searchLinkedIn = linkedin.LinkedInSearch(word, 100)
        searchLinkedIn.do_search_linkedin()

        # from SearchFunctions import otx
        # searchOTX = otx.OTXSearch(word)
        # searchOTX.do_search_otx()

        # from SearchFunctions import portscanner
        # searchPortScan = portscanner.PortScanSearch(word)
        # searchPortScan.do_search_portscan()

        # from SearchFunctions import threatcrowd
        # searchThreatCrowd = threatcrowd.ThreatCrowdSearch(word)
        # searchThreatCrowd.do_search_threatcrowd()

        # from SearchFunctions import virustotal
        # searchVirusTotal = virustotal.VirusTotalSearch(word)
        # searchVirusTotal.do_search_virustotal()

        from SearchFunctions import yahoo
        searchYahoo = yahoo.YahooSearch(word, 100)
        searchYahoo.do_search_yahoo()

        rgx = Regexs(word)
        rgx.getEmails()

        rgx.getFileUrls()
        rgx.getHostnames()
        rgx.getLinkedInLinks()
        rgx.getLinkedInProfiles()
             
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