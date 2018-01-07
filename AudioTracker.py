
class AudioTracker(object):
    def __init__(self, audioText):
        # self.audio = audio
        ### if it is a search
        # creating a search list for detection
        searchVal = "search"
        # checking if search command exist in input audio
        if searchVal in audioText:
            #calling google search function
            self.googleSearch(audioText)    
        else:
            print("Search is not in audio")
        

    def googleSearch(self, audioText):
        # to detect where is search in audio
        try:
            searchIndex = audioText.find("search")
            print(searchIndex)
        except ValueError:
            print("yes")
        pass
        


