from os import listdir, path
from os.path import isfile, join
import os
import shutil

def arrange_files(mypath):
    _files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in _files:
        file_ext = file.split('.')[1]
        new_folder_name=mypath+'/'+ file_ext + '_folder'
        if path.exists(new_folder_name+'/'+file) is not True:
            #print('file ext: {} and new folder name {}'.format(file_ext, new_folder_name))
            if os.path.isdir(new_folder_name) is not True:
                print('creating new folder {}'.format(new_folder_name))
                os.mkdir(new_folder_name)
            print('checking if file {} exists {}'.format(file, path.exists(new_folder_name+'/'+file)))
            shutil.move(join(mypath, file),new_folder_name)
            print('successfully moved file from {} to {}'.format(join(mypath, file), new_folder_name))
        else:
            print("skipping as file exists: {}".format(file))

if __name__== "__main__":
    arrange_files("/Users/adminnc/Downloads")
