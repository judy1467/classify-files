import os
import shutil

print('This program classifies the file by extensions.\n')
print('input dir path:')

def classify_file(file, extension):
    if os.path.isdir(src+'\\'+extension) == False:
        os.mkdir(src+'\\'+extension)
    shutil.move(src+'\\'+file, src+'\\'+extension+'\\'+file)

src = input()

try:
    file_list = os.listdir(src)

except:
    print('path error')
    exit(1)

for i in file_list:
    _, file_extension = os.path.splitext(i)
    if(i in '.' == True):
        print('name         : ' + _)
        print('extension is : ' + file_extension[1:] +'\n')
        classify_file(i, file_extension[1:])

print('done!')