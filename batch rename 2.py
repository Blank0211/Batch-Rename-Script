import os
from sys import argv 
 
file_list = os.listdir()
file_list.sort()
script = os.path.basename(argv[0])

new_name = input('Rename to: ')
num = int(input('Starting number: ')) 


for f in file_list:
    if f == script:
        continue 
    
    f_name, f_ext = os.path.splitext(f)
    os.rename(f, f'{new_name.title()} - {num}{f_ext}')
    num +=1
    
    
print(os.listdir())

