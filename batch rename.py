import os 

folder1 = input('Files\' Location: ')
os.chdir(folder1)
file_list = os.listdir()
file_list.sort()

new_name = input('Rename to: ')
num = int(input('Starting number: ')) 


for f in file_list:
    
    f_name, f_ext = os.path.splitext(f)
    os.rename(f, f'{new_name.title()} - {num}{f_ext}')
    num +=1
    
print(os.listdir())
