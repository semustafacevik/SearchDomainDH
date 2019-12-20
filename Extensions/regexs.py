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

    

    def getTotalResult(self):
        for value in result.values():
            self.totalResult += value + ' * '

    def unique(self) -> list:
        return list(set(self.temp))
