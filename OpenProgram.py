import os

class OpenPregramClass(object):
    def __init__(self, fileName):
        try:
            os.system(fileName+'.exe')
        except Exception as e:
            print(e)
        pass
    
    # for other programs