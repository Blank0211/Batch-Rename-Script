import os 
file1 = 'c:/users/s/desktop/renametest.txt'
folder1 = 'c:/users/s/desktop/mass rename'
os.chdir(folder1)

filelist = os.listdir()

new_name = input('Name: ')
num = int(input('Starting number: ')) 


for f in filelist:
    os.rename(f, '{} {}.txt'.format(new_name, num))
    num +=1

print(os.listdir())
