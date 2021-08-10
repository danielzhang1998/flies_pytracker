import numpy as np
import matplotlib.pyplot as plt
import glob
import sys

def main():
    print(sys.argv)
    d = loadData()
    dataSummary(d)
    totalMotionInROI(d)

def totalMotionInROI(d):
    numROI = np.shape(d)[1]
    xPos = np.arange(numROI) + 1
    totalMotion = np.sum(d,0)
    f,a = plt.subplots(1,1,figsize=(8,4))
    a.bar(xPos,totalMotion)
    plt.xticks(xPos,[str(a) for a in xPos])
    plt.xlabel('ROI')
    plt.ylabel('Total motion\n(displaced pixels)')
    plt.show()
    

def dataSummary(d):
    print('Number of ROI: ', np.shape(d)[1])
    print('Number of frames: ', np.shape(d)[0])

def loadData(dataType='dpix'):
	print('Loading .npy files')
	filenames = sorted(glob.glob(dataType+'*.npy'))

	if len(filenames) > 0: # checks to see if there are any files
		firstFile = filenames.pop(0)
	else:
		sys.exit('No .npy files to analyze')

	data = np.load(firstFile)

	if len(filenames) > 0:
		for f in filenames:
			d = np.load(f)
			data = np.vstack((data,d))
	return data

if __name__ == "__main__":
    main()
