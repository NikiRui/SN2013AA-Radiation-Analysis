import os, sys, subprocess
import pyfits
import matplotlib.pyplot as plt
import numpy as np
from pylab import*

cat_path_rp = '/transit/results_ChangXu/Project/match_rp/'
image_path_rp = '/transit/results_ChangXu/Project/sn2013aa_rp/'

cat_list_rp = []
for root, dirs, files in os.walk(cat_path_rp):
    for filename in files:
        if filename.endswith('.cat'):
            cat_list_rp.append(root+filename)

image_list_rp = []
for root, dirs, files in os.walk(image_path_rp):
    for filename in files:
        if filename.endswith('.fits'):
            image_list_rp.append(root+filename)
    #print 'scanning   '+filename

sn2013aa_rp=[]
image_time_list_rp=[]
for cat_location_rp in cat_list_rp:
    data=np.loadtxt(cat_location_rp)
    x=data[:,0]
    mag0=data[:,4]
    mag=data[:,16]
    R=[]
    R0=[]
    index=cat_list_rp.index(cat_location_rp)
    for j in range(len(x)):
	if (x[j] == 310.943):
            R.append(mag[j])
	    R0.append(mag0[j])
        if (x[j] == 248.370):       
            R.append(mag[j])
            R0.append(mag0[j])
	if (x[j] == 991.235):       
            R.append(mag[j])
            R0.append(mag0[j])
	if (x[j] == 1216.592):       
            R.append(mag[j])
            R0.append(mag0[j])
    for k in range(len(x)):
	    if (x[k] == 1050.126):
		if len(R) != 0:
		    sn2013aa_rp.append(mag[k]*sum(R0)/sum(R))
   		    image=pyfits.open(cat_location_rp.replace(cat_path_rp,image_path_rp).replace('lsc1m004_kb77_20130222_PSNJ143233_rp_l','l').replace('_matched.cat','.fits'))
		    date_str = image[0].header['MJD-OBS']
		    image_time_list_rp.append(date_str)
    print 'rp plot complete   ', np.int(index), '/75'


plt.plot(image_time_list_rp,sn2013aa_rp,'yo')
plt.ylim(-13,-19.5)
#plt.xlim(56534.26,56370.31)
#plt.savefig('plottest2.pdf')
plt.show()
