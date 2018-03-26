import os
import subprocess

class OpenProgramClass(object):
    def __init__(self, fileName):
        self.fileName = fileName.lower()                
        # changing commands for specific programs
        self.changeExeNames()
        # opening programs
        try:
            os.system(self.fileName+'.exe')
        except Exception as e:
            print(e)
        pass
    

    # to change .exe names
    def changeExeNames(self):
        # if calculator so change the exe name
        if 'calculator' in self.fileName:
            self.fileName = 'calc'
        elif 'cmd' in self.fileName:          
            subprocess.call('start', shell=True)
        pass
    # for other programs
    def openCustomPrograms(self):
        
        pass
        