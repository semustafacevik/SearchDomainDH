from Extensions.functions import *
import re

class Regexs:

    def __init__(self, word):

        self.word = word
        self.totalResult = ''
        self.getTotalResult()
        self.disinfectedResult = self.totalResult
        self.temp = []


    def cleanResult(self):

        self.disinfectedResult = self.disinfectedResult.replace("<title>", " ").replace("</title>", " ")\
            .replace("<p>", " ").replace("/p", " ").replace("<cite>", " ").replace("</cite>", " ")\
            .replace("&quot", " ").replace("&nbsp", " ").replace("<span>", " ").replace("</span>", " ")

        dirtyItems = [
            "<em>",
            "</em>",
            "<b>",
            "</b>",
            "%2f",
            "%3a",
            "<strong>",
            "</strong>",
            "<wbr>",
            "</wbr>",
            "<",
            ">",
            ":",
            "=",
            ";",
            "&",
            "%3A",
            "%3D",
            "%3C",
            "/",
            "\\"]

        for dirtyItem in dirtyItems:
            self.disinfectedResult = self.disinfectedResult.replace(dirtyItem, "")

    def getFileUrls(self):

        print('\nSearching File Urls...')
        result['resultFileUrls'] = ''

        regex_fileUrls = re.compile('<a href="(.*?)"')
        self.temp = regex_fileUrls.findall(self.totalResult)
        allUrls = self.unique()
        for url in allUrls:
            if (url.count('doc') or url.count('ppt') or url.count('pdf') or url.count('xls') or url.count('csv')) and not url.count('translat') :
                result['resultFileUrls'] += url + ' * '
            else:
                pass
        
        print('OK - File Urls!')


    def getHostnames(self):

        print('\nSearching Hostnames...')
        result['resultHostnames'] = ''

        regex_hostnames = re.compile(r'[a-zA-Z0-9.-]*\.' + self.word)
        self.temp = regex_hostnames.findall(self.totalResult)
        hostnames = self.unique()
        for hostname in hostnames:
            if(hostname.startswith('2f')):
                hostname = hostname.replace('2f','')
            result['resultHostnames'] += hostname + ' * '
        
        print('OK - Hostnames!')


    def getLinkedInLinks(self):

        print('\nSearching LinkedIn Links...')
        result['resultLinkedInLinks'] = ''

        linkedInResult = result['result_linkedin']
        linkedInResult = linkedInResult.replace('tr.linkedin.com', 'www.linkedin.com')
        regex_linkedInLinks = re.compile(r"url=https:\/\/www\.linkedin.com(.*?)&")
        self.temp = regex_linkedInLinks.findall(linkedInResult)
        for link in self.temp:
            result['resultLinkedInLinks'] += 'https://www.linkedin.com' + link + ' * '
        
        print(result['resultLinkedInLinks'])
        print('OK - LinkedIn Links!')


    def getLinkedInProfiles(self):

        print('\nSearching LinkedIn Profiles...')
        result['resultLinkedInProfiles'] = ''

        linkedInResult = result['result_linkedin']
        linkedInResult = linkedInResult.replace('&amp;', '&')
        regex_linkedInProfiles = re.compile(r"[\w.,_ |\\/&-]* [\-|\|]* LinkedIn")
        self.temp = regex_linkedInProfiles.findall(linkedInResult)
        for profile in (self.temp):
            profile = profile.replace(' | LinkedIn', '').replace(' - LinkedIn', '')
            if profile != " ":
                result['resultLinkedInProfiles'] += profile + ' * '

        print(result['resultLinkedInProfiles'])
        print('OK - LinkedIn Profiles!')


    def getTotalResult(self):
        for value in result.values():
            self.totalResult += value + ' * '

    def unique(self) -> list:
        return list(set(self.temp))
