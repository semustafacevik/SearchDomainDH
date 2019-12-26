from Extensions.functions import *
import re


class Regexs:

    def __init__(self, word):

        self.word = word
        self.totalResult = ''
        self.getTotalResult()
        self.disinfectedResult = self.totalResult
        self.cleanResult()
        self.temp = []

    def cleanResult(self):

        dirtyItems = [
            "<title",
            "</title>",
            "<p",
            "</p>",
            "<div",
            "</div>",
            "<cite",
            "</cite>",
            "&quot;",
            "&nbsp;",
            "&#32",
            "q=",
            "x22@",
            "<span",
            "</span>",
            "mail",
            "Mail",
            "posta",
            "Posta"]

        for dirtyItem in dirtyItems:
            self.disinfectedResult = self.disinfectedResult.replace(dirtyItem, " ")

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

    def getEmails(self):
        
        print('\nSearching Emails...')
        result_response['resultEmails'] = ''

        regex_emails = re.compile(r"[\w_-]+(?:\.[\w_-]+)*@(?:[\w0-9](?:[\w0-9-]*[\w0-9])?\.)+[\w0-9](?:[\w0-9-]*[\w0-9])")
        self.temp = regex_emails.findall(self.disinfectedResult)
        emails = self.unique()

        for email in emails:
            #################################if(email.count(hhtp))
            result_response['resultEmails'] += '¨' + email
        
        print('OK - Emails!')
    
    def getFileUrls(self):

        print('\nSearching File Urls...')
        result_response['resultFileUrls'] = ''

        regex_fileUrls = re.compile('<a href="(.*?)"')
        self.temp = regex_fileUrls.findall(self.totalResult)
        allUrls = self.unique()
        for url in allUrls:
            if (url.count('doc') or url.count('ppt') or url.count('pdf') or url.count('xls') or url.count('csv')) and not url.count('translat') :
                result_response['resultFileUrls'] += '¨' + url
            else:
                pass
        
        print('OK - File Urls!')


    def getHostnames(self):

        print('\nSearching Hostnames...')
        result_response['resultHostnames'] = ''

        regex_hostnames = re.compile(r'[a-zA-Z0-9.-]*\.' + self.word)
        self.temp = regex_hostnames.findall(self.totalResult)
        hostnames = self.unique()
        for hostname in hostnames:
            if(not hostname.startswith('2f') and not hostname[0].isdigit()):
                result_response['resultHostnames'] += '¨' + hostname

        print('OK - Hostnames!')


    def getLinkedInLinks(self):

        print('\nSearching LinkedIn Links...')
        result_response['resultLinkedInLinks'] = ''

        linkedInResult = result['result_linkedin']
        linkedInResult = linkedInResult.replace('tr.linkedin.com', 'www.linkedin.com')
        regex_linkedInLinks = re.compile(r"url=https:\/\/www\.linkedin.com(.*?)&")
        self.temp = regex_linkedInLinks.findall(linkedInResult)
        for link in self.temp:
            result_response['resultLinkedInLinks'] += '¨' + 'https://www.linkedin.com' + link
        
        print('OK - LinkedIn Links!')


    def getLinkedInProfiles(self):

        print('\nSearching LinkedIn Profiles...')
        result_response['resultLinkedInProfiles'] = ''

        linkedInResult = result['result_linkedin']
        linkedInResult = linkedInResult.replace('&amp;', '&')
        regex_linkedInProfiles = re.compile(r"[\w.,_ |\\/&-]* [\-|\|]* LinkedIn")
        self.temp = regex_linkedInProfiles.findall(linkedInResult)
        for profile in (self.temp):
            profile = profile.replace(' | LinkedIn', '').replace(' - LinkedIn', '')
            if profile != " ":
                result_response['resultLinkedInProfiles'] += '¨' + profile

        print('OK - LinkedIn Profiles!')

    def getTotalResult(self):
        for value in result.values():
            self.totalResult += value + ' * '

    def unique(self) -> list:
        return list(set(self.temp))
