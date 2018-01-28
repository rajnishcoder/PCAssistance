# test for finding all exe files
import os
import glob

pwd=os.getcwd() #use later in case you want to return to present dirctory later
os.chdir(r"C:\Program Files")
exe_list=[]
for i in glob.glob('*.exe'):
    exe_list.append(i)
    print(exe_list)

print(exe_list)
for i in exe_list:
   print ('{} :: {}'.format(exe_list.index(i),i))

ind=int(input('Enter index of prog :: '))
os.system(exe_list[ind])