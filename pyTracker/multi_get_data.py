import os

def get_npy():
    '''loop each folder in current folder and find the .npy files'''
    folder = [each for each in os.listdir('.') if os.path.isdir(each)]
    #print(folder)
    for each in folder:
        os.chdir(each)
        files = os.listdir('.')
        for every in files:
            if '.npy' in every:
                import pyTracker.get_data as get_data
                get_data.main()
                break
        os.chdir('..')

get_npy()
        
