import os
import subprocess

class OpenProgramClass(object):
    def __init__(self, fileName):
        print('here')
        # changing commands for specific programs
        progName = fileName.lower()
        # if calculator so change the exe name
        if 'calculator' in progName:
            progName = 'calc'

        elif 'cmd' in progName:
            subprocess.call('start', shell=True)
        # opening programs
        try:
            os.system(progName+'.exe')
        except Exception as e:
            print(e)
        pass
    
    # for other programs
    def openCustomPrograms(args):
        
        pass
        