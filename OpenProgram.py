import os

class OpenPregram(object):
    def __init__(self, fileName):
        try:
            os.startfile(fileName)
        except Exception, e:
            print str(e)