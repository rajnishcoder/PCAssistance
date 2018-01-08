
class AudioTracker(object):
    def __init__(self, audioText):
        # self.audio = audio
        ### if it is a search
        # creating a search list for detection
        searchVal = ["search", "what is"]
        # checking if search command exist in input audio
        for sItem in searchVal:
            if sItem in audioText:
            # if any(x in audioText for x in searchVal):
                print("in")
                #calling google search function
                self.googleSearch(audioText)
                break
            else:
                print("Search is not in audio")
        

    def googleSearch(self, audioText):
        # to detect where is search in audio
        try:
            searchIndex = audioText.index("search")
            print(searchIndex)
        except ValueError:
            print("search not found")
        pass



