import numpy as np

import analysisTools
data = analysisTools.loadData('dpix')
analysisTools.saveDataAsCSV(data,'100204-10-11')
#print("Perm"+str(type(data)))
#print(data.max(axis=0))
#print(data.min(axis=0))
#np.sum(d,0)


#analysisTools.binData(data,60)
#import trackingTools
#trackingTools.setupVidInfo()
#print(vidInfo)
#trackingTools.saveVidInfo()
