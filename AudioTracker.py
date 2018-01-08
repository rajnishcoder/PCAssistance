from GoogleSearch import GoogleSearchClass

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
            if sItem in audioText:
            # if any(x in audioText for x in searchVal):
                # calling google search function
                self.googleSearchIndex(audioText, sItem)
                break
            else:
                print("Search is not in audio")
        

    def googleSearchIndex(self, audioText, sItem):
        # to detect where is search in audio
        try:
            searchIndex = audioText.index(sItem)
            if searchIndex > 0:
                self.googleSearch(audioText)
            else:
                audioText.remove("search")
                print(audioText)
                GoogleSearchClass(audioText)
                print(searchIndex)
        except ValueError:
            print("search not found")
        pass



