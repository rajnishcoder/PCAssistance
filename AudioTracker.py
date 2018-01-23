from GoogleSearch import GoogleSearchClass
from OpenProgram import OpenPregramClass 
# import ast

class AudioTracker(object):
    def __init__(self, audioText):
        ### if it is a search
        self.googleSearch(audioText)
        

    def googleSearch(self, audioText):
        # creating a search list for detection
        searchKeywords = ["search", "what is", "tell me about"]
        # checking if search command exist in input audio
        for sItem in searchKeywords:
            if audioText.index("open") == 0:
                self.callOpenProgram(audioText)
                break
            else:
            # filter search keyword in audio
                if sItem in audioText:
                    # calling google search function
                    self.googleSearchIndex(audioText, sItem)
                    break
        

    # to detect where is search in audio
    def googleSearchIndex(self, audioText, sItem):
        try:
            searchIndex = audioText.index(sItem)
            if searchIndex > 0:
                self.googleSearch(audioText)
            else:
                searchText = audioText.replace(sItem, "")
                GoogleSearchClass(searchText)
        except ValueError:
            print("search not found")
        pass
    
    # for opening programs Class
    def callOpenProgram(self, audioText):
        filteredText = audioText.replace("open", "")
        OpenPregramClass(filteredText)
        pass

        



