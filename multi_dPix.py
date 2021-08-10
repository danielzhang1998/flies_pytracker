import os
# for mac, use 'pip3'
from natsort import natsorted

PATH = '/Volumes/Disk/new'

def make_bash(dir):
    """
    make a bash file

    Args:
        dir: the directory of each sub (child) folder directory
    """

    os.chdir(dir)
    path = ''
    L = []
    for root, dirs, files in os.walk('.'):
        # make the file name sorted with order
        # can not use sort() here
        # for example, if we have list1 = ['1.mp4', '10.mp4', '2.mp4'], then sort() it will be ['1.mp4', '10.mp4', '2.mp4'], not what we want
        # that is why use natsorted() here

        files = natsorted(files)
        for file in files:
            # only solve the .mp4 files, some files on mac might end with '.mp4' but start with '._', need to skip them
            if os.path.splitext(file)[1] == '.mp4' and file.startswith('.') == False and 'output.mp4' in file:
                file_path = os.path.join(root, file)
                if file_path.startswith('./.') == False:
                    file_path = file_path[1:]
                    L.append(file_path)

    if len(L):
        # generate bash files
        path = os.getcwd()
        # print(L)
        with open('run_dpix.bash', 'w') as f:
            f.write("#! /bin/bash\n\n")
            for l in L:
                f.write(f"cd {os.path.split(path + l)[0]}\n")
                f.write(
                    f"python3 {os.path.split(path + l)[0]}/pyTracker/dPix.py {os.path.split(path + l)[-1]} 15 n\n")


if __name__ == '__main__':
    make_bash(PATH)
