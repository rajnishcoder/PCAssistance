# test for finding all exe files
# import os
# import glob

# pwd=os.getcwd() #use later in case you want to return to present dirctory later
# os.chdir(r"C:\Program Files")
# exe_list=[]
# for i in glob.glob('*.exe'):
#     exe_list.append(i)
#     print(exe_list)

# print(exe_list)
# for i in exe_list:
#    print ('{} :: {}'.format(exe_list.index(i),i))

# ind=int(input('Enter index of prog :: '))
# os.system(exe_list[ind])

import os

exe_list=[]

for root, dirs, files in os.walk("."):
#  print(dirs)
 for j in dirs:
  for i in files:
   if i.endswith('.exe'):
     #p=os.getcwd()+'/'+j+'/'+i
     p=root+'/'+j+'/'+i
    #  print(p)
     exe_list.append(p)


for i in exe_list :
  print('index : {} file :{}'.format(exe_list.index(i),i.split('/')[-1]))

ip=int(input('Enter index of file :'))

print('executing {}...'.format(exe_list[ip]))
os.system(exe_list[ip])