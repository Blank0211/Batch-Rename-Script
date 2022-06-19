import os 

folder1 = input('Files\' Location: ')
os.chdir(folder1)
filelist = os.listdir()

new_name = input('Rename to: ')
num = int(input('Starting number: ')) 


for f in filelist:
    os.rename(f, f'{new_name.title()} - {num}.txt')
    num +=1

print(os.listdir())
