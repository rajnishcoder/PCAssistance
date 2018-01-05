import webbrowser

class gSearchClass(object):
    def __init__(self, search):
        self.search = search
        print(search);
        url = "https://www.google.com.tr/search?q={}".format(search)
        webbrowser.open(url)

# set search value 
search = gSearchClass("My search");
# call the class variable
search 


