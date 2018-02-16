import webbrowser

class GoogleSearchClass(object):
    def __init__(self, search):
        # self.search = search
        url = "https://www.google.com.tr/search?q={}".format(search)
        webbrowser.open(url)

# # set search value 
# search = GoogleSearchClass("My search");
# # call the class variable
# search 


