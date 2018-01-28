import os


class OpenPregramClass(object):
    def __init__(self, fileName):
        print('here')
        # changing commands for specific programs
        if 'calculator' in fileName:
            fileName = 'calc'

            # opening programs
            try:
                os.system(fileName+'.exe')
            except Exception as e:
                print(e)
            pass
    
    # for other programs
    def openCustomPrograms(args):
        
        pass
        