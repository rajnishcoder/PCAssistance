from GoogleSearch import GoogleSearchClass
import ast

class AudioTracker(object):
    def __init__(self, audioText):
        # self.audio = audio
        ### if it is a search
        self.googleSearch(audioText)
        

    def googleSearch(self, audioText):
        # creating a search list for detection
        searchVal = ["search", "what is", "tell me about"]
        # checking if search command exist in input audio
        for sItem in searchVal:
            # filter search keyword in audio
            if sItem in audioText:
            # if any(x in audioText for x in searchVal):
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



