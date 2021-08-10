import os
# for mac, use 'pip3'
from natsort import natsorted

# A terminal font formatter
STYLE = {
    'fore': {
        'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
        'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37,
    },
    'back': {
        'black': 40, 'red': 41, 'green': 42, 'yellow': 43,
        'blue': 44, 'purple': 45, 'cyan': 46, 'white': 47,
    },
    'mode': {
        'bold': 1, 'underline': 4, 'blink': 5, 'invert': 7,
    },
    'default': {
        'end': 0,
    }
}


def use_style(string, mode='', fore='', back=''):
    """
    a function to change terminal print() output color

    Args:
        string: string need to print
        mode: font mode
        fore: font color
        back: background color
    """
    mode = '%s' % STYLE['mode'][mode] if mode in STYLE['mode'] else ''
    fore = '%s' % STYLE['fore'][fore] if fore in STYLE['fore'] else ''
    back = '%s' % STYLE['back'][back] if back in STYLE['back'] else ''
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, string, end)


'''
def test():
    print(use_style('Normal'))
    print(use_style('Bold', mode='bold'))
    print(use_style('Underline & red text', mode='underline', fore='red'))
    print(use_style('Invert & green back', mode='reverse', back='green'))
    print(use_style('Black text & White back', fore='black', back='white'))
'''


# change the PATH here, to be the directory of the parent folder which contains the child folder (.mp4 is inside of the child folder)
PATH = os.getcwd()

# get the .mp4 file names under current working directory
os.chdir(PATH)


def merge_mp4(dir):
    """
    make a bash file, then convert .mp4 file to be the .ts file. finally merge the .ts files and convert to a large .mp4 file

    Args:
        dir: the directory of each sub (child) folder directory
    """

    # go into the sub (child) folder
    os.chdir(dir)
    L = []
    for root, dirs, files in os.walk('.'):
        # make the file name sorted with order
        # can not use sort() here
        # for example, if we have list1 = ['1.mp4', '10.mp4', '2.mp4'], then sort() it will be ['1.mp4', '10.mp4', '2.mp4'], not what we want
        # that is why use natsorted() here

        files = natsorted(files)
        for file in files:
            # only solve the .mp4 files, some files on mac might end with '.mp4' but start with '._', need to skip them
            if os.path.splitext(file)[1] == '.mp4' and file.startswith('.') == False:
                file_path = os.path.join(root, file)
                L.append(file_path)

        if len(L):
            # generate bash files
            with open('concat_mp4.sh', 'w') as f:
                f.write("#! /bin/bash\n\n")
                for l in L:
                    f.write(
                        f"ffmpeg -i {l} -vcodec copy -acodec copy -vbsf h264_mp4toannexb {l.replace('.mp4', '.ts')}\n")

                f.write(
                    f'\nffmpeg -i "concat:{"|".join([i.replace(".mp4", ".ts") for i in L])}" -acodec copy -vcodec copy -absf aac_adtstoasc output.mp4\n')
                f.write('rm *.ts')

    # run the bash file to start merge and convert to be .mp4 file
    os.system('bash concat_mp4.sh')

    # back to the parent folder
    os.chdir('..')


if __name__ == '__main__':
    list1 = os.listdir('.')
    list1 = natsorted(list1)
    for each in list1:
        if each.startswith('.') == False and os.path.isdir(each):
            print(use_style('Currently processing folder: '+each,
                            mode='reverse', fore='black', back='white'))
            merge_mp4(each)
